from django.db import models
from django.db.models import fields
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from .models import Post
from .forms import ImageForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy


# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'

class PostListHome(ListView):
    model = Post
    template_name = 'home.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostUpdateView(UpdateView):
    model = Post
    fields = ['body']
    template_name = 'post_edit.html'

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = ImageForm    
    template_name = 'post_new.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
