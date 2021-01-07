from django.shortcuts import render, get_object_or_404, redirect
from students.forms import StudentForm
from staff.forms import StaffForm
from students.models import Student
from staff.models import Staff
from common.models import AppUser
from .methods import id_generator
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password, UserAttributeSimilarityValidator

# Create your views here.

def login_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():
            details = form.cleaned_data
            username_input = details['username']
            passwd_input = details['passwd']

            try:
                if not AppUser.objects.filter(username=username_input):
                    raise ValidationError('User does not exist')
            except ValidationError as e:
                form.add_error('username',e)
                return render(request, 'common/home.html', {'form': form})

            credentials = AppUser.objects.get(username=username_input)
            correct_username = credentials['username']
            correct_password = credentials['passwd']
            
            try:
                if str(passwd_input) != str(correct_password):
                    raise ValidationError('Incorrect password')
            except ValidationError as e:
                form.add_error('passwd',e)
                return render(request, 'common/home.html', {'form': form})

    return render(request, 'common/home.html', {'form': form})

def admin_login(request,*args,**kwargs):
    return render(request,"admins/home.html")

def registration_view(request,*args,**kwargs):
    return render(request,"common/register.html")

def account_created_view(request,*args,**kwargs):
    return render(request,"common/account_created.html")

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
            new_account_id = id_generator()
            
            try:
                validate_password(new_passwd, form)
            except ValidationError as e:
                form.add_error('passwd', e)
                return render(request, "common/studentregistration.html", {'form': form})
            

            # try:
            #     user_credentials = [new_username, new_fName, new_lName, new_mName, new_mobile, new_enrolment]
            #     for item in user_credentials:
            #         if item.lower() in new_passwd.lower():
            #             raise ValidationError('Password too similar to credentials...')
            # except ValidationError as e:
            #     form.add_error('passwd', e)
            #     return render(request, "common/studentregistration.html", {'form': form})
            

            newStudent = Student(firstName=str(new_fName.capitalize()),
                        middleName=str(new_mName.capitalize()),
                        lastName=str(new_lName.capitalize()),
                        username=str(new_username),
                        passwd=str(new_passwd),
                        account_id=str(new_account_id),
                        enrolment=str(new_enrolment),
                        date=str(new_dob),
                        mobile=str(new_mobile),
                        branch=str(new_branch),
                        sem=str(new_sem),
                        email=str(new_email.lower()),
                        gender=str(new_gender),
                        isPending=True
                        )

            newUser = AppUser(
                        firstName=str(new_fName.capitalize()),
                        lastName=str(new_lName.capitalize()),
                        username=str(new_username),
                        passwd=str(new_passwd),
                        email=str(new_email.lower()),
                        category='Student',
                        isAdmin=False,
                        isPending=True
            )
            newStudent.save()
            # Student.objects.create(**form.cleaned_data)
            return redirect("../pending-account")
    else:
        form = StudentForm(request.POST or None)
        for field in form.errors:
                form[field].field.widget.attrs['class'] += 'error'


    return render(request,"common/studentregistration.html",{'form':form})

def pending_account_view(request,*args,**kwargs):
    return render(request,"common/pending_account.html")

def staff_registration(request,*args,**kwargs):
    if request.method == "POST":
        form = StaffForm(request.POST or None)
        if form.is_valid():
            details = form.cleaned_data
            new_username = details['username']
            new_fName = details['firstName']
            new_mName = details['middleName']
            new_lName = details['lastName']
            new_passwd = details['passwd']
            new_email = details['email']
            new_dob = details['date']
            new_gender = details['gender']
            new_mobile = details['mobile']
            new_branch = details['branch']
            new_designation = details['designation']
            new_isAdmin = False
            new_isPending = True
            new_account_id = id_generator()

            #sets category of user
            new_category = ''
            if new_designation in ['Professor', 'Assistant Professor']:
                new_category = 'Faculty'
            elif new_designation == 'Head of Department':
                new_category = 'Head of Department'
            elif new_designation in ['Lab Instructor','Lab Assistant']:
                new_category = 'Staff'
            

            # find the number of users in staff
            staff_count = int(Staff.objects.count())

            # if there are no staff members, the first created user will be admin
            if staff_count < 1:
                new_isAdmin = True
                new_category = 'Admin'
                new_isPending = False

            try:
                validate_password(new_passwd, form)
            except ValidationError as e:
                form.add_error('passwd', e)
                return render(request, "common/staffregistration.html", {'form': form})
            
            # try:
            #     user_credentials = [new_username, new_fName, new_lName, new_mName, new_mobile]
            #     for item in user_credentials:
            #         if item.lower() in new_passwd.lower():
            #             raise ValidationError('Password too similar to credentials.')
            # except ValidationError as e:
            #     form.add_error('passwd', e)
            #     return render(request, "common/staffregistration.html", {'form': form})

            newStaff = Staff(
                        firstName=str(new_fName.capitalize()),
                        middleName=str(new_mName.capitalize()),
                        lastName=str(new_lName.capitalize()),
                        username=str(new_username),
                        passwd=str(new_passwd),
                        account_id=str(new_account_id),
                        date=str(new_dob),
                        mobile=str(new_mobile),
                        branch=str(new_branch),
                        email=str(new_email.lower()),
                        gender=str(new_gender),
                        designation=str(new_designation),
                        isAdmin=new_isAdmin,
                        isPending=new_isPending
                        )
            
            newUser = AppUser(
                        firstName=str(new_fName.capitalize()),
                        lastName=str(new_lName.capitalize()),
                        username=str(new_username),
                        passwd=str(new_passwd),
                        email=str(new_email.lower()),
                        category=str(new_category),
                        isAdmin=new_isAdmin,
                        isPending=new_isPending
            )
            newStaff.save()
            newUser.save()

            if new_isPending:
                return redirect("../pending-account")
            else:
                return redirect("../account-created")
    else:
        form = StaffForm(request.POST or None)
        for field in form.errors:
                form[field].field.widget.attrs['class'] += 'error'

    return render(request,"common/staffregistration.html",{'form':form})

