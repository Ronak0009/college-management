from django import forms
from students.models import student1

class StudentForm(forms.ModelForm):
    gender_choice=(('M','Male'),
                   ('F','Female'),
                   ('O','Other'))

    # college_choices=(('Uvpce','U.V Patel'),
    #                    ('Bspp','B.S Patel'))

    branch_choices=(('Ce','Computer Engineering'),
                    ('It','Information Technology '),)  

    sem_choices=(('1','I'),
                       ('2','II'),
                       ('3','III'),)   
    fullname = forms.CharField(label='Full Name:',
                widget=forms.TextInput(attrs={"placeholder":"Your Full name",
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

    enrollment = forms.CharField(label='Enrollment Number:',
                widget=forms.TextInput(attrs={"placeholder":"Your enrolment number",
                                             "size":"40",
                                             "class":"text"}))
    mobile=forms.CharField(label='Mobile:',
                widget=forms.TextInput(attrs={"placeholder":"Your mobile number",
                                             "size":"40",
                                             "class":"text"}))
   
    gender=forms.ChoiceField(label="Gender:",choices=gender_choice,
                         widget=forms.Select(attrs={
                             "class":"choice1",})) 

    # college=forms.ChoiceField(label="Name of College:",choices=college_choices,
    #                      widget=forms.Select(attrs={
    #                          "class":"choice2",})) 
    branch=forms.ChoiceField(label="Branch:",choices=branch_choices,
                         widget=forms.Select(attrs={
                             "class":"choice3",})) 
    sem=forms.ChoiceField(label="Semester:",choices=sem_choices,
                         widget=forms.Select(attrs={
                             "class":"choice4",})) 
    
                          
    date = forms.CharField(label="Date of Birth:",
                widget=forms.TextInput(attrs={
                    "placeholder":"dd/mm/yyyy",
                    "class":"datefield",
                    'type':"date"
                }))
    email = forms.EmailField(label="Email:", required=False,
                widget=forms.EmailInput(attrs={"placeholder":"Your email",
                                             "size":"40",
                                             'type':"email",
                                             "class":"text"}))
    class Meta:
        model = student1
        fields= [
            'enrollment',
            'fullname',
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

    def clean_firstName(self, *args, **kwargs):
        name = self.cleaned_data.get("firstName")
        print(name)
        if "purvesh" in name.lower():
            print("This is a good name!")
            name += " Gandhi"
            return name
        else:
            raise forms.ValidationError("Bad name!")

class RawStudentForm(forms.Form):
    firstName = forms.CharField()
    lastName = forms.CharField()
    enrollment = forms.CharField()
    