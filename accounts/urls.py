from django.urls import path
from .views import loginPageView

urlpatterns = [
    path('login/', loginPageView.as_view(), name='login'),
]