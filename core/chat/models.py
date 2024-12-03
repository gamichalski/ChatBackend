from django.db import models

from core.authUser.models import User

class Chat(models.Model):
    class SelectedIa(models.IntegerChoices):
        LINGUAGENS = 1, "Português"
        EXATAS = 2, "Matematica"
        CIENCIAS_NATURAIS = 3, "Ciências Naturais"
        CIENCIAS_HUMANAS = 4, "Ciêncisa Humanas"
        REDAÇÂO = 5, "Redação"
        GENERICA = 6, "Genérica"
    chat_name = models.CharField(max_length=255)
    ia = models.IntegerField(choices=SelectedIa.choices, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="chat", null=True, blank=True)

class Answer(models.Model):
    answer = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    chat = models.ForeignKey(Chat, on_delete=models.PROTECT, related_name="asnwer")
    
    @property
    def theme(self):
        return self.chat.ia





