from os import name, stat
from django.urls import path
from .views import loginPageView, signupPageView


urlpatterns = [
    path('', loginPageView.as_view(), name="login"),
    path('signup/', signupPageView.as_view(), name="signup"),
]