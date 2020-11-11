from django.contrib import admin

# Django
from django.contrib import admin

# Models
from apps.posts.models import (
  Post,
  Category,
  Tag
)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  """Post model admin."""

  list_display = (
    'title',
    'author',
    'status',
  )

  search_fields = (
    'slug_name',
    'title',
  )

  list_filter = (
    'status',
  )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  """Category model admin."""

  list_display = (
    'name',
  )

  search_fields = (
    'name',
  )

  list_filter = ()

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
  """Tag model admin."""

  list_display = (
    'name',
  )

  search_fields = (
    'name',
  )

  list_filter = ()
