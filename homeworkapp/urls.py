"""Define URL pattern for homeoworkapp."""

from django.urls import path
from . import views

app_name = 'homeworkapp'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    #Page that shows course information
    path('courses/', views.courses, name='courses'),
    #Page that shows a certain courses homework
    path('course/<int:course_id>', views.course, name='course'),
    #Page for adding a new course
    path('new_course/', views.new_course, name='new_course'),
    #Path for adding a new homework
    path('new_homework/<int:course_id>/', views.new_homework, name='new_homework'),
    #Path for editing a homework page418
    path('edit_homework/<int:homework_id>/', views.edit_homework, name='edit_homework'),
]