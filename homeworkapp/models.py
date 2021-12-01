from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    course_name = models.CharField(max_length=200, default='0')
    teacher = models.CharField(max_length=200, default='0')
    semester = models.CharField(max_length=200, default='0')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course_name

class Homework(models.Model):
    course = models.ForeignKey(Course, default=Course, on_delete=models.CASCADE)
    assignment = models.CharField(max_length=200, default='0')
    deadline = models.DateTimeField()
    materials = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default = False)
    owner = models.ForeignKey(User, default=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.assignment
