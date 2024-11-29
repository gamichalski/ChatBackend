from core.chatgptIA.helpers.gpt_config import gptChat
from django.db.models.signals import post_save
from django.dispatch import receiver
from core.chatgptIA.models import GenericAI

@receiver(post_save, sender=GenericAI)
def update_response(instance, sender, created, **kwargs):
    if created:
        instance.response = gptChat(instance.answer)
        instance.save()