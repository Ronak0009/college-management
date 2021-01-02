from django import forms
from students.models import Student
from staff.models import Staff
from django.contrib.auth.password_validation import validate_password
from django.utils.safestring import mark_safe
import re

class StudentForm(forms.ModelForm):
    error_css_class = 'error'
    required_css_class = 'required'

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
    passwd = forms.CharField(label='Password:',  min_length=8, max_length=40,
                widget=forms.PasswordInput(attrs={"placeholder":"Create a password",
                                             "size":"40",
                                             "class":"text"}))
    confirm_passwd = forms.CharField(label='Confirm Password:',min_length=8, max_length=40,
                widget=forms.PasswordInput(attrs={"placeholder":"Re-enter your password",
                                             "size":"40",
                                             "class":"text"}))

    enrolment = forms.CharField(label='Enrolment Number:', max_length=15,
                widget=forms.TextInput(attrs={"placeholder":"Your enrolment number",
                                             "size":"40",
                                             "class":"text"}))
    mobile = forms.CharField(label='Mobile:', max_length=10,
                widget=forms.TextInput(attrs={"placeholder":"Your mobile number",
                                             "size":"40",
                                             "class":"text"
                                             }))
   
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

    date = forms.DateField(label="Date of Birth:",
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
            'username',
            'enrolment',
            'date',
            'gender',
            'passwd',
            'confirm_passwd',
            'email',
            'mobile',
            'branch',
            'sem',
        ]
    
    def clean(self, *args, **kwargs):
        cleaned_data = super().clean()
        firstName = str(self.cleaned_data.get("firstName"))
        middleName = str(self.cleaned_data.get("middleName"))
        lastName = str(self.cleaned_data.get("lastName"))
        passwd = str(self.cleaned_data.get("passwd"))
        confirm_passwd = str(self.cleaned_data.get("confirm_passwd"))
        username = str(self.cleaned_data.get("username"))
        mobile = str(self.cleaned_data.get("mobile"))
        email = str(self.cleaned_data.get("email"))
        enrolment = str(self.cleaned_data.get("enrolment"))

        # validates first name
        try:
            if not re.search("^[A-Za-z]+$", firstName):
                fn_error = "Not a valid first name"
                raise forms.ValidationError(fn_error)
        except forms.ValidationError as e:
            self.add_error('firstName', e)
        
        # validates middle name
        try:
            if middleName != '' and middleName != None:
                if not re.search("^[A-Za-z]+$", middleName):
                    mn_error = "Not a valid middle name"
                    raise forms.ValidationError(mn_error)
        except forms.ValidationError as e:
            if middleName != '' or middleName != None:
                self.add_error('middleName', e)
        
        # validates last name
        try:
            if not re.search("^[A-Za-z]+$", lastName):
                ln_error = "Not a valid last name"
                raise forms.ValidationError(ln_error)
            else:
                pass
        except forms.ValidationError as e:
            self.add_error('lastName', e)

        # validates enrolment number
        try:
            if not re.search("^[0-9]*$", enrolment):
                en_error = "Not a valid enrolment number"
                raise forms.ValidationError(en_error)
        except forms.ValidationError as e:
            self.add_error('enrolment', e)
        
        # checks if enrolment already exists
        try:
            if Student.objects.filter(enrolment=enrolment).exists():
                enrolment_exists_error = enrolment + " is already associated</br>with another account."
                enrolment_exists_error = mark_safe(enrolment_exists_error)
                raise forms.ValidationError(enrolment_exists_error)
        except forms.ValidationError as e:
            self.add_error('enrolment', e)

        # validates password safety
        try:
            if not re.search('^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$',passwd):
                errormsg = mark_safe('Password must contain at least</br>1 upper case letter,</br>1 lower case letter,</br>1 digit and 1 special symbol.')
                raise forms.ValidationError(errormsg)
        except forms.ValidationError as e:
            self.add_error('passwd', e)

        # checks if password and confirm password are same
        try:
            if passwd != confirm_passwd:
                raise forms.ValidationError('Passwords do not match')
        except forms.ValidationError as e:
            self.add_error('confirm_passwd', e)
        
        # checks if username already exists
        try:
            if Student.objects.filter(username=username).exists() or Staff.objects.filter(username=username).exists():
                username_exists_error = username + ' is already taken.</br>Select a different username.'
                username_exists_error = mark_safe(username_exists_error)
                raise forms.ValidationError(username_exists_error)
        except forms.ValidationError as e:
            self.add_error('username', e)

        # validates username
        try:
            if not re.search(r'^\w+$', username):
                username_error = mark_safe("Username can only contain alphanumeric</br>characters and the underscore.")
                raise forms.ValidationError(username_error)
        except forms.ValidationError as e:
            self.add_error('username', e)

        # validates mobile number
        try:
            if not re.search("^[0-9]{10}$",mobile):
                mobile_error = "Not a valid phone number"
                raise forms.ValidationError("Not a valid phone number")
        except forms.ValidationError as e:
            self.add_error('mobile', e)
        
        # checks if mobile is already used
        try:
            if Student.objects.filter(mobile=mobile).exists() or Staff.objects.filter(mobile=mobile).exists():
                mobile_exists_error = 'This mobile number is already</br>associated with an account.'
                mobile_exists_error = mark_safe(mobile_exists_error)
                raise forms.ValidationError(mobile_exists_error)
        except forms.ValidationError as e:
            self.add_error('mobile', e)

        # validates email
        try:
            if not re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', email):
                email_error = "Not a valid email"
                raise forms.ValidationError(email_error)
        except forms.ValidationError as e:
            self.add_error('email', e)
        
        # checks if email is already used
        try:
            if Student.objects.filter(email=email).exists() or Staff.objects.filter(email=email).exists():
                email_exists_error = 'This email is already associated</br>with an account'
                email_exists_error = mark_safe(email_exists_error)
                raise forms.ValidationError(email_exists_error)
        except forms.ValidationError as e:
            self.add_error('email', e)
        else:
            return cleaned_data


    # def clean_username(self, *args, **kwargs):
    #     username = self.cleaned_data.get("username")
    #     if Student.objects.filter(username=username).exists() or Staff.objects.filter(username=username).exists():
    #         error = username + ' is already taken. Select a different username.'
    #         raise forms.ValidationError(error)
    #     elif not  re.search(r'^\w+$', username):
    #         raise forms.ValidationError("Username can only contain alphanumeric characters and the underscore.")
    #     else:   
    #         return username
       
    
    # def clean_mobile(self, *args, **kwargs):
    #     mobile = self.cleaned_data.get("mobile")
    #     if re.search("^[0-9]*$",mobile):
    #         return mobile
    #     else:
    #         raise forms.ValidationError("Not a valid phone number")
            
    # def clean_passwd(self, *args, **kwargs):
    #     passwd = self.cleaned_data.get("passwd")
    #     if not re.search('^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$',passwd):
    #         errormsg = mark_safe('Password must contain at least</br>1 upper case letter,</br>1 lower case letter,</br>1 digit and 1 special symbol.')
    #         raise forms.ValidationError(errormsg)
    #     else:
    #         return passwd
        
    # def clean_firstName(self, *args, **kwargs):
    #     name = self.cleaned_data.get("firstName")
    #     print(name)
    #     if "purvesh" in name.lower():
    #         print("This is a good name!")
    #         name += " Gandhi"
    #         return name
    #     else:
    #         raise forms.ValidationError("Bad name!")


    