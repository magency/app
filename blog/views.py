# Create your views here.
#-*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import logout, authenticate, login
from django.core.urlresolvers import reverse
from datetime import datetime
from blog.models import *
from blog.forms import *
from django.contrib.auth.models import User
from django import template
from django.db import IntegrityError
from django.template import VariableDoesNotExist
from django.contrib.auth.decorators import login_required
from django.http import *


global user

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
 
def form_contact(request):
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

@login_required(redirect_field_name='to')
def new_comment(request):
    sauvegarde = False
 
    if request.method == "POST":
           form = NewCommentForm(request.POST, request.FILES)
           if form.is_valid():
                   com = Comment()
                   com.name = form.cleaned_data["name"]
                   com.comment = form.cleaned_data["adress"]
                   com.photo = form.cleaned_data["photo"]
                   com.save()
 
                   sauvegarde = True
    else:
           form = NewCommentForm()
    name="Nassim BENHARRAT"
    current_date= datetime.now() 
    return render(request, 'blog/contact2.html',locals())  

@login_required(redirect_field_name='to')
def view_comment(request):
    global user
    name="Nassim BENHARRAT"
    current_date= datetime.now()
    comments = Comment.objects.all()
    return render(request, 'blog/view_contact.html', locals())    

def subscribe(request):
    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = ProfileForm(request.POST)  # Nous reprenons les données

        if form.is_valid(): # Nous vérifions que les données envoyées sont valides   
            username = form.cleaned_data["username"] 
            password1 = form.cleaned_data["password1"] 
            password2 = form.cleaned_data["password2"]

            
            if password1==password2:
              try: 
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                send = True
              except IntegrityError:
                notValidateUser= True  
            else:
              notValidatePass= True  
            
    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        form = ProfileForm()  # Nous créons un formulaire vide
    name="Nassim BENHARRAT"
    current_date= datetime.now()
    return render(request, 'blog/subscribe.html', locals())

def connexion(request):
    global user
    error = False
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]  # Nous récupérons le nom d'utilisateur
            password = form.cleaned_data["password"]  # … et le mot de passe
            user = authenticate(username=username, password=password)  #Nous vérifions si les données sont correctes 
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
            else: #sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()

    name="Nassim BENHARRAT"
    current_date= datetime.now()    
    return render(request, 'blog/connexion.html',locals())      

def deconnexion(request):                                                                               
    logout(request) 
    return redirect(reverse(connexion))    

def sign_in_first(request):#not integrated yet in the code
  name="Nassim BENHARRAT"
  current_date= datetime.now()
  return render(request, 'blog/alert.html', locals())  

def say_hello(request):
  if request.user.is_authenticated():
    return HttpResponse("hello, {0} !".format(request.user.username))
  return HttpResponse("Hello, anonymous.")  

