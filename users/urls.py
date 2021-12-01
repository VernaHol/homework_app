#Defines URL patterns for users

from django.urls import path, include

from . import views

app_name = 'users'
url_patterns = [
    #Include default auth paths
    path('', include('django.contrib.auth.urls')),
    #Registration page
    path('register/', views.register, name='register'),
]