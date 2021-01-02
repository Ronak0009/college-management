from django.shortcuts import render, get_object_or_404, redirect
from students.forms import StudentForm
from staff.forms import StaffForm
from students.models import Student
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password, UserAttributeSimilarityValidator

# Create your views here.

def login_view(request, *args, **kwargs):
    return render(request, "common/home.html")

def admin_login(request,*args,**kwargs):
    return render(request,"admins/home.html")

def registration_view(request,*args,**kwargs):
    return render(request,"common/register.html")

def student_registration(request,*args,**kwargs):
    if request.method == "POST":
        form = StudentForm(request.POST or None)
        if form.is_valid():
            details = form.cleaned_data
            new_passwd = details['passwd']
            new_username = details['username']
            new_fName = details['firstName']
            new_mName = details['middleName']
            new_lName = details['lastName']
            new_email = details['email']
            new_enrolment = details['enrolment']
            new_dob = details['date']
            new_gender = details['gender']
            new_mobile = details['mobile']
            new_branch = details['branch']
            new_sem = details['sem']

            try:
                validate_password(new_passwd, form)
            except ValidationError as e:
                form.add_error('passwd', e)
                return render(request, "common/studentregistration.html", {'form': form})
            
            try:
                user_credentials = [new_username, new_fName, new_lName, new_mName, new_mobile, new_enrolment]

                for item in user_credentials:
                    if item.lower() in new_passwd.lower():
                        raise ValidationError('Password too similar to credentials')
            except ValidationError as e:
                form.add_error('passwd', e)
                return render(request, "common/studentregistration.html", {'form': form})
            
            
            

            newStudent = Student(firstName=str(new_fName.capitalize()),
                        middleName=str(new_mName.capitalize()),
                        lastName=str(new_lName.capitalize()),
                        username=str(new_username),
                        passwd=str(new_passwd),
                        enrolment=str(new_enrolment),
                        date=str(new_dob),
                        mobile=str(new_mobile),
                        branch=str(new_branch),
                        sem=str(new_sem),
                        email=str(new_email.lower()),
                        gender=str(new_gender)
                        )
            newStudent.save()


            # Student.objects.create(**form.cleaned_data)
            return redirect("../login")
    else:
        form = StudentForm(request.POST or None)
        for field in form.errors:
                form[field].field.widget.attrs['class'] += 'error'

    return render(request,"common/studentregistration.html",{'form':form})

def staff_registration(request,*args,**kwargs):
    f=StaffForm()
    return render(request,"common/staffregistration.html",{'form':f})

