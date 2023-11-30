from django.conf import settings
from django.db import models

class Chat(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    message = models.TextField()
    response = models.CharField(max_length=200, default='')
    created_at = models.DateTimeField(auto_now_add=True)
