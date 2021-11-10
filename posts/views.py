from django.views.generic import ListView, DetailView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ('title', 'body', 'image', 'author')
    template_name = 'post_new.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)