"""Define URL pattern for homeoworkapp."""

from django.urls import path
from . import views_by_ns

app_name = 'homeworkapp'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
]