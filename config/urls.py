"""config URL Configuration

The `urlpatterns` list routes URLs to views. 
"""
# Django imports
from django.urls import include, re_path, path
from django.contrib import admin
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
    openapi.Info(
        title="Django React chat API",
        default_version="v1",
        description="An simple chat application based on Django and React",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("admin/", admin.site.urls, name="admin_interface"),
    path("v1/auth/", include("apps.authentication.urls")),
    path("v1/chat/", include("apps.chat.urls")),
]
