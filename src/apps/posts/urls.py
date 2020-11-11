"""Posts URLs."""

# Django
from django.urls import path

# Views
from apps.posts.views import list_posts, create_post


urlpatterns = [
  path('posts/', list_posts),
  path('posts/create/', create_post)
]