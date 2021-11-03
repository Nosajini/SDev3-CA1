from django.urls import path
from .views import homePageView, loginPageView

urlpatterns = [
    path('', homePageView.as_view(), name='home'),
    path('login/', loginPageView.as_view(), name='login'),
]

