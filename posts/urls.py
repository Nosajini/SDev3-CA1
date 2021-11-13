from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('new/', PostCreateView.as_view(), name='post_new'),
    path('<uuid:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('<uuid:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('<uuid:pk>/delete/', PostDeleteView.as_view(), name='post_delete')
]
