from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# Create your models here.
class CustomUser(AbstractUser):
    location = models.TextField(null=True, blank=True, max_length=30);


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), null=True, on_delete=models.CASCADE,)
    date_of_birth = models.DateField(blank=False, null=False)

    def __str__(self):
        return str(self.user)