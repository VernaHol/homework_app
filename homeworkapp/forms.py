from django import forms
from .models import Course, Homework

#page 410
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['text']
        labels = ['text': '']

class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ['text']
        labels = ['text': '']

 