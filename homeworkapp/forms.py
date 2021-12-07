from django import forms
from django.forms import widgets
from .models import Course, Homework

#page 410
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['text']
        labels = {'text': ''}

#page 414
class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols':100})}

 