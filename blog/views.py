# Create your views here.
#-*- coding: utf-8 -*-

from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from datetime import datetime
from blog.models import *
from blog.forms import *


def home(request):
  text = """<h1>WELCOME PAGE</h1>
            <p>MA PREMIERE PAGE HTML SOUS PYTHON/DJANGO!</p>
            <a href="http://localhost:8000/data/" target="_blank">TO DATA PAGE</a>"""
  return HttpResponse(text)

def data(request):
  text = """<h1>DATA PAGE</h1>
            <href>MA PREMIERE PAGE HTML SOUS PYTHON/DJANGO!</p>
            <a href="http://localhost:8000/welcome/" target="_blank">TO WELCOME PAGE </a>"""
  return HttpResponse(text)

def view_object(request, id_object):
  #VIEW WHICH RETURNS AN OBJECT NUMBER
  if (int(id_object))>100: #Si l'ID est supérieur à 100, nous considérons que l'article n'existe pas
        raise Http404
  text = "<p>Vous avez demandé l'object n°{0} !</p>".format(id_object)
  return HttpResponse(text)

def view_object_date(request, day, month, year):
  #Liste des articles d'un mois précis
  text = "Vous avez demandé l'object de la date {0}/{1}/{2}.".format(day, month, year)
  return HttpResponse(text)  

def test_html(request): 
  name="Nassim BENHARRAT"
  current_date= datetime.now()
  return render(request, 'blog/test.html', locals())

def generate_index(request): 
  name="Nassim BENHARRAT"
  current_date= datetime.now()
  obj = Object.objects.all() # Nous sélectionnons tous nos articles
  return render(request, 'blog/index.html', locals())

def read(request, id, slug):
  try:
    obj = Object.objects.get(id=id, slug=slug)
  except Object.DoesNotExist:
    raise Http404
  
  name="Nassim BENHARRAT"
  current_date= datetime.now()

  return render(request, 'blog/read_object.html', locals())  
 
def contact(request):
    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = MessageForm(request.POST)  # Nous reprenons les données
 
        if form.is_valid(): # Nous vérifions que les données envoyées sont valides
 
            # Ici nous pouvons traiter les données du formulaire
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            returnMessage = form.cleaned_data['returnMessage']
 
            # Nous pourrions ici envoyer l'e-mail grâce aux données que nous venons de récupérer
 
            send = True
 
    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        form = MessageForm()  # Nous créons un formulaire vide
    name="Nassim BENHARRAT"
    current_date= datetime.now()
    return render(request, 'blog/contact.html', locals())

def new_contact(request):
    sauvegarde = False
 
    if request.method == "POST":
           form = NewContactForm(request.POST, request.FILES)
           if form.is_valid():
                   contact = Contact()
                   contact.name = form.cleaned_data["name"]
                   contact.adress = form.cleaned_data["adress"]
                   contact.photo = form.cleaned_data["photo"]
                   contact.save()
 
                   sauvegarde = True
    else:
           form = NewContactForm()
    name="Nassim BENHARRAT"
    current_date= datetime.now() 
    return render(request, 'blog/contact2.html',locals())    