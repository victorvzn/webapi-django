# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Utilities
from apps.utils.models import BaseModel


class Post(BaseModel):
  """Post model.
  """

  class StatusChoices(models.TextChoices):
    PUBLIC = 'PU', _('Public')
    PRIVATE = 'PR', _('Private')
    TRASH = 'TR', _('Trash')

  title = models.CharField('title', max_length=140)
  slug_name = models.SlugField(unique=True, max_length=140)
  content = models.TextField('content', blank=True, null=True)
  excerpt = models.TextField('excerpt', blank=True, null=True)
  picture = models.ImageField(upload_to='posts/pictures', blank=True)
  status = models.CharField(
    'status',
    max_length=2,
    choices=StatusChoices.choices,
    default=StatusChoices.PRIVATE
  )

  category = models.ManyToManyField('posts.Category', blank=True)
  tags = models.ForeignKey('posts.Tag', on_delete=models.CASCADE, blank=True, null=True)

  author = models.ForeignKey('users.User', on_delete=models.CASCADE)

  def __str__(self):
    """Return title."""
    return self.title
  
  class Meta(BaseModel.Meta):
    """Meta class."""

    ordering = ['-modified', '-created']