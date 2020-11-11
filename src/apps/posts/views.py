"""Posts views."""

# Django REST Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Models
from apps.posts.models import Post
from apps.users.models import User

#Serializers
from apps.posts.serializers import (
  PostSerializer,
  PostCreateSerializer,
)

@api_view(['GET'])
def list_posts(request):
  """List posts."""
  posts = Post.objects.filter(status=Post.StatusChoices.PUBLIC)
  serializer = PostSerializer(posts, many=True)
  return Response(serializer.data)

@api_view(['POST'])
def create_post(request):
  """Create post."""
  serializer = PostCreateSerializer(data=request.data)
  serializer.is_valid(raise_exception=True)
  # post = serializer.save(author=request.user)
  author = User.objects.get(pk=1)
  post = serializer.save(author=author)
  return Response(PostSerializer(post).data)
