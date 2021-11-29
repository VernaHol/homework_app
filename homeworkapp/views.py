from django.shortcuts import render

# Create your views here.

def index(request):
    """The home page of the Course"""
    return render(request, 'homeworkapp/index.html')