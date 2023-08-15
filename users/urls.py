"""Defines URL patterns for users"""
from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')),
    # Sign up page.
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    ]