from django.db import models
from core.authUser.models import User

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    qrcode_key = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, default='pending')
    ticket_url = models.CharField(max_length=255, blank=True, null=True)
    instalments = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.user.email} - {self.amount}'