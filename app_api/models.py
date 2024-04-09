from django.db import models
from django.contrib.auth.models import User

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.db import connection
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)



class CustomToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    token = models.CharField(max_length=255, unique=True)

class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    model = models.CharField(max_length=100)
    a = models.CharField(max_length=20, null=True)
  
    class Meta:
        app_label = "app_api"
   