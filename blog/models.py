#-*- coding: utf-8 -*-
from django.db import models

# Create your models here.
 
class MessageCategory(models.Model):
    name = models.CharField(max_length=30)
 
    def __unicode__(self):
        return self.nom

class Message(models.Model):
	title = models.CharField(max_length=100)
   	user = models.CharField(max_length=42)
   	content = models.TextField(null=True)
   	date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Post date")
 	category = models.ForeignKey('MessageCategory')
 	
   	def __unicode__(self):
   	    return u"%s" % self.title

