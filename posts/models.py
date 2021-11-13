import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='post')
    body = models.TextField(max_length=1245)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
    
    class Meta():
        ordering = ('date',)
