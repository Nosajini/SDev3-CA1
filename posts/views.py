from django.shortcuts import get_object_or_404, render
from django.db import models
from django.views.generic import ListView, DetailView
from .models import Post, Board
from .forms import ImageForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy


# Create your views here.

class PostList(ListView):
    model = Post

    def get(self, request, board_id=None):
        board = None
        posts = None
        if board_id != None:
            board = get_object_or_404(Board, id = board_id)
            posts = Post.objects.filter(board = board)
        else:
            posts = Post.objects.all()
        
        return render(request, "post_list.html", {'board':board, 'posts':posts})


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'

class PostListHome(ListView):
    model = Post
    template_name = 'home.html'

class PostDetailView(DetailView):
    model = Post

    def get(self, request, board_id, post_id):
        try:
            post = Post.objects.get(board_id = board_id, id = post_id)
        except Exception as e:
            raise e
        return render(request, "post_detail.html", {'post':post})
        #template_name = 'post_detail.html'

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['body']
    template_name = 'post_edit.html'
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = ImageForm    
    template_name = 'post_new.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
