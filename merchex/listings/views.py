from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band, Listing

def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""
            <h1>Hello World!</h1>
            <p>Les groupes en bases :</p>
            <ul>
                <li>{bands[0].name}</li>
                <li>{bands[1].name}</li>
                <li>{bands[2].name}</li>
            </ul>
            """)

def about(request):
    return HttpResponse("<h1>A propos</h1> <p>Un paragraphe html</p>")

def contact(request):
    return HttpResponse("<h1>Contact</h1> <p>Formulaire</p>")

def annonces(request):
    l = Listing.objects.all()
    return HttpResponse(f"""
            <h1>listing</h1> 
            <p>Liste des annonces</p>
            <ol>
                <li>{l[0].title}</li>
                <li>{l[1].title}</li>
                <li>{l[2].title}</li>
                <li>{l[3].title}</li>
            </ol>
            """)

