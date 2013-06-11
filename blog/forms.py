#-*- coding: utf-8 -*-
from django import forms
from models import Message

class ContactForm(forms.Form):
	subject = forms.CharField(max_length=100)
	message = forms.CharField(widget=forms.Textarea)
	sender = forms.EmailField(label=u"Votre adresse mail")
	returnMessage=forms.BooleanField(label=u"Renvoi de mail", help_text=u"Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)

class MessageForm(forms.ModelForm):
	class Meta:
		model = Message

class NewContactForm(forms.Form):
    name = forms.CharField()
    adress = forms.CharField(widget=forms.Textarea)
    photo = forms.FileField()	