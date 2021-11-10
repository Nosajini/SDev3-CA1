from os import name, stat
from django.urls import path
from .views import loginPageView, signupPageView, change_passPageView


urlpatterns = [
    path('', loginPageView.as_view(), name="login"),
    path('signup/', signupPageView.as_view(), name="signup"),
    path('password_change/', change_passPageView.as_view(), name="change_pass")
]