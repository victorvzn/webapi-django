"""Development settings."""

from .base import *  # NOQA


# Base

DEBUG = True


# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = '7cswzu4m6$z+3s4ta87$-^gjngd6g%+id015)u&soy=q_)*i%+'

ALLOWED_HOSTS = [
    "localhost",
    "0.0.0.0",
    "127.0.0.1",
]

# Email

EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.console.EmailBackend')

EMAIL_HOST = 'localhost'

EMAIL_PORT = 1025


# django-extensions

INSTALLED_APPS += ['django_extensions']  # noqa F405
