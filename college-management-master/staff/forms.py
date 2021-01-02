from django import forms
from staff.models import Staff

class StaffForm(forms.ModelForm):
    gender_choice=(('M','Male'),
                   ('F','Female'),
                   ('O','Other'))

    role_choices=(('S','Student'),
                        ('F','Faculty'),)

    branch_choices= Staff.branch_choices
  
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
    mobile=forms.CharField(label='Mobile:',
                widget=forms.TextInput(attrs={"placeholder":"Your mobile number",
                                             "size":"40",
                                             "class":"text"}))
   
    gender=forms.ChoiceField(label="Gender:",choices=gender_choice,
                         widget=forms.Select(attrs={
                             "class":"choice1"})) 

    role=forms.ChoiceField(label="Your Role:",choices=role_choices,
                          widget=forms.Select(attrs={
                              "class":"choice2",})) 
    branch=forms.ChoiceField(label="Branch:",choices=branch_choices,
                         widget=forms.Select(attrs={
                             "class":"choice3",})) 
                          
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
        model = Staff
        fields= [
            'firstName',
            'middleName',
            'lastName',
            'date',
            'gender',
            'username',
            'passwd',
            'confirm_passwd',
            'email',
            'mobile',
            'branch',
            'role',
        ]

    def clean_firstName(self, *args, **kwargs):
        pass
    