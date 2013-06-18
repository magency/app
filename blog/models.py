#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime



# Create your models here.
 
class MessageCategory(models.Model):
    name = models.CharField(max_length=30)
 
    def __unicode__(self):
        return self.name

class Message(models.Model):
	title = models.CharField(max_length=100)
   	user = models.CharField(max_length=42)
   	content = models.TextField(null=True)
   	date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Post date")
 	category = models.ForeignKey('MessageCategory')

   	def __unicode__(self):
   	    return u"%s" % self.title

class Object(models.Model):
    slug = models.SlugField(max_length=100)
	
    def __unicode__(self):
        return self.slug

class Comment(models.Model):
    name = models.CharField(max_length=255)
    comment = models.TextField()
    photo = models.FileField(upload_to="media/")
 
    def __unicode__(self):
       	return self.name

    def is_recent(self):
        "Return true if the comment is posted in the last 30 days"
        return (datetime.now()-self.date).days < 30    

    class Meta:
        permissions = (
                ("view_comments","comments"),
        )            
