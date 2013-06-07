# Create your views here.
#-*- coding: utf-8 -*-

from django.http import HttpResponse, Http404

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
  if not(int(id_object)): #Si l'ID est supérieur à 100, nous considérons que l'article n'existe pas
        raise Http404
  text = "<p>Vous avez demandé l'object n°{0} !</p>".format(id_object)
  return HttpResponse(text)

def view_object_date(request, day, month, year):
  #Liste des articles d'un mois précis
  text = "Vous avez demandé l'object de la date {0}/{1}/{2}.".format(day, month, year)
  return HttpResponse(text)  