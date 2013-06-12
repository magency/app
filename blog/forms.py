#-*- coding: utf-8 -*-
from django import forms
from models import *

class ContactForm(forms.Form):
	subject = forms.CharField(max_length=100)
	message = forms.CharField(widget=forms.Textarea)
	sender = forms.EmailField(label=u"Votre adresse mail")
	returnMessage=forms.BooleanField(label=u"Renvoi de mail", help_text=u"Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)

class MessageForm(forms.ModelForm):
	class Meta:
		model = Message

class ProfileForm(forms.Form):
	username = forms.CharField(label="Username", max_length=30)
	password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
	password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput)

class NewContactForm(forms.Form):
    name = forms.CharField()
    adress = forms.CharField(widget=forms.Textarea)
    photo = forms.FileField()	

class ConnexionForm(forms.Form):
	username = forms.CharField(label="USER", max_length=30)
	password = forms.CharField(label="PASSWORD", widget=forms.PasswordInput)    