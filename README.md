# Installation :
## Création de l'environnement de développement

```
python3 -m venv env
source env/bin/activate

pip3 install django
pip3 freeze > requirements.txt
```

## Configuration du projet
Création du code de base pour l'application
```
django-admin startproject merchex
```

Execution du serveur
```
python3 manage.py runserver
```
accessible via http://127.0.0.1:8000

Création de la base de données
```
python3 manage.py migrate
```
fichier db.sqlite3 créé

## Création de la première application
```
python3 manage.py startapp listings
```
dossier de l'application listings créé sous merchex/

-> Ajouter 'listings' dans INSTALLED\_APPS dans merchex/merchex/settings.py


# Création d'une vue. 
La vue est ce que le client va voir.
-> listings/views.py

une fonction de vue prend en paramètre un objet HttpRequest (qui doit s'appeler request par convention)
elle retourne toujours un objet HttpResponse

ajouter la vue listings dans merchex/merchex/urls.py

# Création d'un modèle
Correspond à une classe d'objet python qui sera convertis et stocké par django dans la base

-> listings/models.py

une fois le modele créer on effectue une migration
```
python3 manage.py makemigrations
python3 manage.py migrate
```

## Création d'objet via le shell de Django

```
>>> from listings.models import Band
>>> band = Band()
>>> band.name = "Soul"
>>> band.save()
>>> band = Band.objects.create(name='Foo Fighters')
>>> band = Band.objects.create(name='Gojira')
>>> Band.objects.count()
>>> Band.objects.all()
```

Récuperationd des objets:
* MODEL.objects.all() > Récupère tous les objets
* MODEL.objects.get(id=VALEUR) > récupération d'un objet par son id


### Utiliser les objets dans les vues.
Récupérer les objets band par exemple dans une des vues de listings/views.py
on appelle pour cela la méthode de classe de la classe d'objet que l'on veut récupérer.


# Utilisation des gabarits
listing/templates/listings/hello.html
La bonne pratique veut que l'on mette un sous répertoire qui porte le nom de l'application en dessous du rep template.

Modification de la fonction de vue (listing/views.py) pour prendre en compte le gabarit

avec l'utilisation de la fonction render, il devient possible d'utiliser les variables de gabarit {{ }}
render(request, 'bands/hello.html', {'bands': bands}) 
-> le 3e argument est un dictionnaire dont les clés sont des variables utilisable dans le code html car transformé par django

Syntaxe itération du for dans django (gabarit)
```
{% for band in bands %}
{{ band.name }}
{% endfor %}
```

Utilisation de filtre pour les variables '|'

```
{{ bands|length }}
{{ bands.1.name|lower }}
{{ bands.1.name|upper }}
```

Utilsation de l'instruction if

```
{% if bands|length < 5 }
	peu de
{% elif bands|length < 10 %}
	quelques
{% else %}
	beaucoup de
{% endif %}
	bal bla

{% if band|lower == 'gojira' %}
	balabal
{% endif %}
```

le gabarit s'occupe de la présentation de la page.
la vue s'occupe de la récupération des données. 


## Utilisation d'un modèle de base pour éviter le DRY
```
<html>
	<head><title>Merchex</title></head>
	<body>

		{% block content %}{% endblock %}
	</body>
</html>
```
block est un espace réservé qui a le nom de content et quio va recevoir du contenu.

reprendre le code de la page qui doit utiliser la base
```
{% extends 'listings/base.html' %}

{% block content %}
... code html spécifique
{% endblock %}
```

### Utilisation de fichier static CSS
créer un fichier /listings/static/listings/style.css

dans le fichier base.html
```
{% load static %}
<html>
	<head>
		<title>Merchex</title>
		<link rel="stylesheet" href={% static 'listings/style.css' %} />
```

le 'static' indique qu'il faut chercher dans le répertoire spécial 'static' de l'application
bien penser à faire le load du static.


### Liaison entre modèle
Utilisation de clé étrangère
```
# ajouter un nouveau champs
band = models.ForeignKey(\<Model de rattachement\>, null=True, on\_delete=models.SET\_NULL)
```



### Informations complémentaire sur les modèles
1.Appliquer des valeurs min et max
2.valeur par défault
3.null autorisé
```
from django.core.validators import MaxValueValidator, MinValueValidator
(validator=[MinValueValidator=1, MaxValueValidator=100])
(default=value)
(null=True, blank=True)
```

# Interface d'administration et CRUD

1. création d'un superuser
```
python3 manage.py createsuperuser
```

Indiquer à Django de gérer les modèles via le site d'administration. 
fichier listings/admin.py

```
from django.contrib import admin
from listings.models import Band

admin.site.register(Band)
```
Accès via IP:PORT/admin


# Les pièges de la migration
## Annuler une migration non désirée

```
# Afficher les migrations
python3 manage.py showmigrations
# Récupérer le nom et applicationde la migration précédente
# Effectuer le rollback
python3 manage.py migrate <Application> <nom de la migration>
python3 manage.py migrate listings 0005\_listing\_band
rm listings/migrations/0006\_band\_like\_new

# solution 2
refaire une migration avec les modifications 

# Fusion de migration
python3 manage.py makemigrations --merge
```

# Interface utilisateur
Accès aux différentes pages, merchex/merchex/urls.py

```
from listings import views

urlpatterns = [
...
	path('bands/', views.band_list, name='band-list'),
	path('bands/<int:id>/', views.band_detail) 
```
Dans listings/views.py
```
def band_detail(request, id):
	return render(request, 'listings/band_detail.html', {'id': id}
```
Dans listings/templates/listings.band\_detail.html
```
{% extends 'listings/base.html' %}

{% block content %}
<h2>L'identifiant est {{ id }}</h2>
{% endblock %}
```

# Réaliser un formulaire
Créer un fichier listings/forms.py
```
from django import forms
class ContactUsForm(forms.Form):
	name = forms.CharField(required=False)
	email = forms.EmailField()
	message = forms.CharField(max_length=1000)
```

Créer la vue : listings/views.py
```
from listings.forms import ContactUsForm

def contact(request):
	form = ContactUsForm()
	return render(request, 'listings/contact.html', {'form': form}
```

Créer le template html : listings/templates/listings/contact.html
```
<form action="" method="post" novalidate>
	{% csrf_token %}
	{{ formi.as_p }}	# as_p pour empiler
	<input type="submit" value="Envoyer">
</form>
```

# Envoyer un mail
Dans la gestion de la vue
listings/views.py
```
from django.shortcuts import render, redirect
import django.core.mail import send_mail

def contact(request):
	if request.method == 'POST':
		form = ContactUsForm(request.POST)

		if form.is_valid():
			send_mail(
				subject=f'Message de {from.cleaned_data["name"] or "anonyme"}',
				message=form.cleaned_data['message'],
				from_email=form.cleaned_data['email'],
				recipient_list=['admin@merchex.xyz']
				)
			return redirect('email-sent')
	else:
		form = ContactUsForm()

	return render(request, 'listings/contact.html', {'form': form}
```

Service de messagerie fictif de django
dans merchex/settings.py
```
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```





