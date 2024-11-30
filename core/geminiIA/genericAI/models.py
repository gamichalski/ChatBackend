from django.db import models
from core.authUser.models import User

class GeminiGenericAi(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    response = models.TextField(null=True, blank=True)
    answer = models.CharField(max_length=4000, blank=True, null=True)
    cover = models.FileField(upload_to='files/', blank=True, null=True)
    
    def __str__(self):
        return self.answer
    
    
    