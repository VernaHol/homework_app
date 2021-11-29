from django.shortcuts import render

# Create your views here.

def index(request):
    """The home page of the Course"""
    return render(request, 'homeworkapp/index.html')

def course(request):
    """show all homeworks."""
    courses = Course.objects.order_by('date_added')
    context = {'courses': courses}
    return render(request, 'homeworkapp/courses.html', context)