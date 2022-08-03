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
>> listings/views.py

une fonction de vue prend en paramètre un objet HttpRequest (qui doit s'appeler request par convention)
elle retourne toujours un objet HttpResponse

ajouter la vue listings dans merchex/merchex/urls.py


