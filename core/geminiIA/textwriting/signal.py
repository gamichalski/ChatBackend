from .models import TextWritingAI
from django.db.models.signals import post_save
from django.dispatch import receiver
from .config_ia import response

@receiver(post_save, sender=TextWritingAI)
def SendResponse(instance, sender, created, **kwargs):
    if created:
        chat_response = response.send_message(instance.answer)
        instance.response = chat_response.text
        instance.save()