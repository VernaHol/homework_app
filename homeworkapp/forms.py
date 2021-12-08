from django import forms
from django.forms import widgets
from .models import Course, Homework

#page 410
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'teacher', 'semester']
        labels = {'course_name':'', 'teacher':'', 'semester': ''}

#page 414
class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ['assignment', 'materials']
        labels = {'assignment': '', 'materials':''}
        widgets = {'assignment': forms.Textarea(attrs={'cols':100}), 'materials': forms.Textarea(attrs={'cols':80}) }

 