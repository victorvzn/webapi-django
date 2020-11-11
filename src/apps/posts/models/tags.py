# Django
from django.db import models

# Utilities
from apps.utils.models import BaseModel


class Tag(BaseModel):
  """Tag model.
  """

  name = models.TextField('name')
  description = models.TextField('description', blank=True, null=True)

  def __str__(self):
    """Return name."""
    return self.name