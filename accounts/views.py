from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.
class loginPageView(TemplateView):
    template_name = 'registration/login.html'

class signupPageView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class change_passPageView(TemplateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('login')
    template_name = 'registration/password_change.html'
