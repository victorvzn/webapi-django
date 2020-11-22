"""Post serializers."""

# Django REST Framework
from rest_framework import serializers

# Models
from apps.posts.models import Post
from apps.posts.models import Category


class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ['name',]


class PostSerializer(serializers.ModelSerializer):
  """Post serializer"""

  category = CategorySerializer(many=True, read_only=True)

  class Meta:
    model = Post
    fields = [
      'title',
      'slug_name',
      'content',
      'excerpt',
      'picture',
      'status',
      'category',
    ]


class PostCreateSerializer(serializers.Serializer):
  """Create a post serializer."""

  title = serializers.CharField(max_length=140)
  slug_name = serializers.SlugField(max_length=140)
  status = serializers.ChoiceField(
    choices=Post.StatusChoices.choices,
    default=Post.StatusChoices.PRIVATE
  )

  def create(self, validated_data):
    """Create post."""
    return Post.objects.create(**validated_data)
