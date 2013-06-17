from django.contrib import admin
from blog.models import MessageCategory, Message, Object, Comment
 
admin.site.register(MessageCategory)
admin.site.register(Message)
admin.site.register(Object)
admin.site.register(Comment)