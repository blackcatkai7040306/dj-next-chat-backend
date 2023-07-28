# Python imports
from os.path import join

# project imports
from .common import *

# uncomment the following line to include i18n
# from .i18n import *


# ##### DEBUG CONFIGURATION ###############################
DEBUG = True

# allow all hosts during development
ALLOWED_HOSTS = ["*"]

# adjust the minimal login
LOGIN_URL = "/admin"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/swagger"


# ##### DATABASE CONFIGURATION ############################

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "chatapp",
        "USER": "postgres",
        "PASSWORD": "pratik",
        "HOST": "localhost",
        "PORT": "5432",
        # "ATOMIC_REQUESTS": True,
    }
}


# ##### APPLICATION CONFIGURATION #########################

INSTALLED_APPS = DEFAULT_APPS + CUSTOM_APPS + INSTALLED_APPS
