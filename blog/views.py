# Create your views here.
#-*- coding: utf-8 -*-

from django.http import HttpResponse

def home(request):
  text = """<h1>APPLICATION TEST</h1>
            <p>MA PREMIERE PAGE HTML SOUS PYTHON/DJANGO!</p>"""


  return HttpResponse(text)



