from django.db import models
from core.authUser.models import User

class LanguagesAI(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.CharField(max_length=4000, blank=True, null=True)
    cover = models.FileField(upload_to='files/', default=None, null=True, blank=True)
    response = models.TextField(blank=True, null=True)









    

