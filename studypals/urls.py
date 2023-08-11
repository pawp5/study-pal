"""Defines URL patterns for users"""
from django.urls import path, include

from . import views

app_name = 'studypals'
urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')),
    # Home page
    path('', views.index, name='index'),
    # Chat page
    path('chat/', views.chat, name='chat'),
    path('dashboard', views.dashboard, name='dashboard'),
    ]