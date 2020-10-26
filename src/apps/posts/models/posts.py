# Django
from django.db import models

# Utilities
from apps.utils.models import BaseModel


class Post(BaseModel):
  """Posts model.

  A post is a 
  """

  title = models.TextField('title')
  content = models.TextField('content')
  excerpt = models.TextField('excerpt')
  status = models.CharField('status', max_length=2)
  type = models.CharField('type', max_length=2)
  picture = models.ImageField(upload_to='posts/pictures', blank=True, null=True)

  author = models.ForeignKey('users.User', on_delete=models.CASCADE)