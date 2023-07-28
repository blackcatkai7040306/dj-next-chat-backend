# Python imports
from os.path import join

# project imports
from .common import *

# uncomment the following line to include i18n
# from .i18n import *


# ##### DEBUG CONFIGURATION ###############################
DEBUG = os.getenv("DEBUG")

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
        "NAME": os.getenv("DATABASE_NAME"),
        "USER": os.getenv("DATABASE_USER"),
        "PASSWORD": os.getenv("DATABASE_PASSWORD"),
        "HOST": os.getenv("DATABASE_HOST"),
        "PORT": os.getenv("DATABASE_PORT"),
        # "ATOMIC_REQUESTS": True,
    }
}


# ##### APPLICATION CONFIGURATION #########################

INSTALLED_APPS = DEFAULT_APPS + CUSTOM_APPS + INSTALLED_APPS
