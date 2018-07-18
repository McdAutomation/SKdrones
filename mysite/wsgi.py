"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)

# -----------------------------------------------------------------------------
# Tries to import local wsgi, if on dev,
# import everything in local_Settings, which overrides the dj_database_url
# If on deploy, local_settings won't be found so just ignore the ImportError
# -----------------------------------------------------------------------------
try:
    from .local_wsgi import *
except ImportError:
    pass