"""Main URL module."""

# Django

from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    # Django Admin

    path('admin/', admin.site.urls),

    # Endpoints

    path('', include(('apps.posts.urls', 'posts'), namespace='posts')),
    path('', include(('apps.users.urls', 'users'), namespace='users')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
