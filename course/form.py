from django import forms 
from .models import * 

class AddCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        exclude = ('author', )

class UpdateCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        exclude = ('author', )