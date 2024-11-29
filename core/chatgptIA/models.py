from django.db import models
from core.authUser.models import User
from django.conf import settings

class GenericAI(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.CharField(max_length=4000)
    response = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.answer

