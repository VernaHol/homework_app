from django.shortcuts import render
from .models import Course

# Create your views here.

def index(request):
    """The home page of the Course"""
    return render(request, 'homeworkapp/index.html')

def courses(request):
    """show all homeworks."""
    courses = Course.objects.order_by('date_added')
    context = {'courses': courses}
    return render(request, 'homeworkapp/courses.html', context)

def course(request, course_id):
    """Shows the individual course and all its homeworks."""
    course = Course.objects.get(id=course_id)
    homeoworks = course.homework_set.order_by('-date_added')
    context = {'course': course, 'homeoworks': homeoworks}
    return render(request, 'homeworkapp/course.html', context)