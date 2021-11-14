from django import forms
from django.db import models
from django import forms
from .models import Post

class ImageForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['board', 'title', 'body', 'image',]
