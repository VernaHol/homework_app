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
    homeworks = course.homework_set.order_by('-date_added')
    context = {'course': course, 'homeworks': homeworks}
    return render(request, 'homeworkapp/course.html', context)

#page411
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

#page415
def new_homework(request, course_id):
    """Adds a new homework to a particuar course"""
    course = course.object.get(id=course_id)

    if request.method != 'POST':
        #No data submitted; create a blank form.
        form = HomeworkForm()
    else:
        # POST data submitted; process data.
        form = HomeworkForm(data=request.POST)
        if form.is_valid():
            new_homework = form.save(commit=False)
            new_homework.course = course
            new_homework.save()
            return redirect('homeworkapp/new_homeworkapp.html', context)

    #Display a blank or invalid form.
    context = {'course': course, 'form': form}
    return render(request, 'homeworkapp/new_homework.html', context)

#page418
def edit_homework(request, homework_id)
    """Edit an existing homework"""
    homework = Homework.objects.get(id=homework_id)
    course = homework.course

    if request.method != 'POST':
        #Initial request; pre-fill form with the current homework
        form = HomeworkForm(instance=homework)
    else:
        #POST data submitted; process data
        form = HomeworkForm(instance=homework, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('homeworkapp:course', course_id=course.id)

context = {'homework': homework, 'course': course, 'form': form}
return render(request, 'homeworkapp/edit_homework.html', context)

      
