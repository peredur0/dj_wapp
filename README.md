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

