"""Define URL pattern for homeoworkapp."""

from django.urls import path
from . import views

app_name = 'homeworkapp'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    #Page that shows course information
    path('courses/', views.courses, name='courses'),
]