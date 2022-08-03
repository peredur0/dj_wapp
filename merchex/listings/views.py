from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("<h1>Hello World!</h1>")

def about(request):
    return HttpResponse("<h1>A propos</h1> <p>Un paragraphe html</p>")

def contact(request):
    return HttpResponse("<h1>Contact</h1> <p>Formulaire</p>")

def annonces(request):
    return HttpResponse("<h1>listing</h1> <p>Liste des annonces</p>")
