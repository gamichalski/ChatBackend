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

class ChatMessage(models.Model):
    class TypeAuthor(models.IntegerChoices):
        USER = 1, "User"
        IA = 2, "Ia"
    author_type = models.IntegerField(choices=TypeAuthor, default=TypeAuthor.IA)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    chat = models.ForeignKey(Chat, on_delete=models.PROTECT, related_name="messages")

    @property
    def author(self):
        if self.author_type == 1:
            return self.chat.user
        else:
            return self.chat.ia
