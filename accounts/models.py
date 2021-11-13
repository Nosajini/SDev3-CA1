from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# Create your models here.
class CustomUser(AbstractUser):
    location = models.TextField(blank=True, max_length=30, default='n/a')

class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), null=True, on_delete=models.CASCADE,)

    def __str__(self):
        return str(self.user)
