from django.views.generic import TemplateView

# Create your views here.
class loginPageView(TemplateView):
    template_name = 'registration/login.html'