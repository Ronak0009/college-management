from django import forms
from students.models import Student

class editforms(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"