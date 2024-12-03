from django.db import models
from core.authUser.models import User

class MathAI(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.CharField(max_length=4000, blank=True, null=True)
    cover = models.FileField(upload_to='files/', default=None, blank=True, null=True)
    response = models.TextField(blank=True, null=True)