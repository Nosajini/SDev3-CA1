from django.urls import path
from .views import loginPageView

urlpatterns = [
    path('', loginPageView.as_view(), name="login"),
]