from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from authentication.views import RegisterView


urlpatterns = [
    path("login/", ObtainAuthToken.as_view()),
    path("register/", RegisterView.as_view()),
]
