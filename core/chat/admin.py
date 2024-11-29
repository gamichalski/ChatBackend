from django.contrib import admin
from .models import Chat, ChatMessage

# Register your models here.
admin.site.register(ChatMessage)
admin.site.register(Chat)