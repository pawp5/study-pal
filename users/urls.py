<<<<<<< HEAD
"""Defines URL patterns for users"""
from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')),
    # Sign up page.
    path('signup/', views.signup, name='signup'),
=======
"""Defines URL patterns for users"""
from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')),
    # Sign up page.
    path('signup/', views.signup, name='signup'),
>>>>>>> 8370b914406d0e7e6cc81cdd76708d4004b83da8
    ]