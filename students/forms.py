from django import forms
from students.models import Student
import django.contrib.auth.password_validation as pwdval

class StudentForm(forms.ModelForm):
    gender_choice=Student.gender_choices

    branch_choices= Student.branch_choices 

    sem_choices=Student.sem_choices

    firstName = forms.CharField(label='First Name:',
                widget=forms.TextInput(attrs={"placeholder":"Your first name",
                                             "size":"40",
                                            "class":"text"}))
    middleName = forms.CharField(label='Middle Name:', required=False,
                widget=forms.TextInput(attrs={"placeholder":"Your middle name (optional)",
                                             "size":"40",
                                            "class":"text"}))
    lastName = forms.CharField(label='Last Name:',
                widget=forms.TextInput(attrs={"placeholder":"Your last name",
                                             "size":"40",
                                            "class":"text"}))
    username = forms.CharField(label='Username:',
                widget=forms.TextInput(attrs={"placeholder":"Your Username",
                                             "size":"40",
                                             "class":"text"}))
    passwd = forms.CharField(label='Password:',
                widget=forms.PasswordInput(attrs={"placeholder":"Create a password",
                                             "size":"40",
                                             "class":"text"}))
    confirm_passwd = forms.CharField(label='Confirm Password:',
                widget=forms.PasswordInput(attrs={"placeholder":"Re-enter your password",
                                             "size":"40",
                                             "class":"text"}))

    enrolment = forms.CharField(label='Enrolment Number:',
                widget=forms.TextInput(attrs={"placeholder":"Your enrolment number",
                                             "size":"40",
                                             "class":"text"}))
    mobile = forms.CharField(label='Mobile:',
                widget=forms.TextInput(attrs={"placeholder":"Your mobile number",
                                             "size":"40",
                                             "class":"text"}))
   
    gender = forms.ChoiceField(label="Gender:",choices=gender_choice,
                         widget=forms.Select(attrs={
                             "class":"choice1",
                             })) 

    branch = forms.ChoiceField(label="Branch:",choices=branch_choices,
                         widget=forms.Select(attrs={
                             "class":"choice3",})) 

    sem = forms.ChoiceField(label="Semester:",choices=sem_choices,
                         widget=forms.Select(attrs={
                             "class":"choice4",})) 

    date = forms.CharField(label="Date of Birth:",
                widget=forms.TextInput(attrs={
                    "placeholder":"dd/mm/yyyy",
                    "class":"datefield",
                    'type':"date"
                }))
    email = forms.EmailField(label="Email:",
                widget=forms.EmailInput(attrs={"placeholder":"Your email",
                                             "size":"40",
                                             'type':"email",
                                             "class":"text"}))
    class Meta:
        model = Student
        fields= [
            'firstName',
            'middleName',
            'lastName',
            'enrolment',
            'date',
            'gender',
            'username',
            'passwd',
            'confirm_passwd',
            'email',
            'mobile',
            'branch',
            'sem',
        ]

    # def clean_firstName(self, *args, **kwargs):
    #     name = self.cleaned_data.get("firstName")
    #     print(name)
    #     if "purvesh" in name.lower():
    #         print("This is a good name!")
    #         name += " Gandhi"
    #         return name
    #     else:
    #         raise forms.ValidationError("Bad name!")


    