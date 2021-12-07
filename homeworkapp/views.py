from django.shortcuts import render, redirect

from .models import Course, Homework
from .forms import CourseForm, HomeworkForm


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

def new_course(request):
    """Add a new course"""
    if request.method != 'POST':
        #No data submitted; create a blank form.
        form = CourseForm()
    else:
        #POST data submitted; process data.
        form = CourseForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('homeworkapp:topics')

    #Displays a blank or invalid form.
    context = {'form': form}
    return render(request, 'homeworkapp/new_course.html', context)



            
