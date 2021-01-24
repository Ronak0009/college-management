from django import forms
from students.models import Student

class editforms(forms.ModelForm):
    class Meta:
        model=Student
        fields= [
            'firstName',
            'middleName',
            'lastName',
            'username',
            'account_id',
            'enrolment',
            'mobile',
            'branch',
            'sem',
            'email',
            'gender',
            'isPending',
        ]