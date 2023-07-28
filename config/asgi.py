"""
ASGI config for config project.
It exposes the ASGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/asgi/
"""

import os
import django
from channels.routing import get_default_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")

django.setup()

application = get_default_application()
