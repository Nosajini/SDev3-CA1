from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class CustomUser(AbstractUser):
    location = models.TextField(blank=True, max_length=30, default='n/a')

class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), null=True, on_delete=models.CASCADE,)
    profile_pic = models.ImageField(upload_to='profilepic/')

    @receiver(post_save, sender=CustomUser)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=CustomUser)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return str(self.user)
