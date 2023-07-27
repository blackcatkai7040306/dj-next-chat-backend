"""config URL Configuration

The `urlpatterns` list routes URLs to views. 
"""
# Django imports
from django.urls import include, re_path
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls', namespace='blog')),
    # provide the most basic login/logout functionality
    re_path(
        r"^login/$",
        auth_views.LoginView.as_view(template_name="core/login.html"),
        name="core_login",
    ),
    re_path(r"^logout/$", auth_views.LogoutView.as_view(), name="core_logout"),
    # enable the admin interface
    re_path(r"^admin/", admin.site.urls),
]
