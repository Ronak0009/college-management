from django.shortcuts import render, redirect
from students.models import Student
from datetime import datetime
from common.forms import LoginForm
from admins.forms import editforms
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import common
from  . import forms


# Create your views here.
@login_required(login_url=common.views.login_view)
def admins_home_view(request, *args, **kwargs):
    time = datetime.now()
    currentTime = time.strftime("%D %I:%M:%S %p")
    context = {
        'timestamp': currentTime,
    }
    return render(request, "admins/home.html",context)

@login_required(login_url=common.views.login_view)
def admins_courses_view(request, *args, **kwargs):
    return render(request, "admins/courses.html")

@login_required(login_url=common.views.login_view)
def admins_students_view(request, *args, **kwargs):
    return render(request, "admins/students.html")

@login_required(login_url=common.views.login_view)
def admins_staff_view(request, *args, **kwargs):
    return render(request, "admins/staff.html")

@login_required(login_url=common.views.login_view)
def admins_profile_view(request, *args, **kwargs):
    return render(request, "admins/profile.html")

# for data extraction
@login_required(login_url=common.views.login_view)
def admins_student_pending_detail_view(request,*args,**kwargs):
    obj=Student.objects.filter(isPending=True)
    print(obj)
    return render(request,"admins/students.html",{'student':obj})

@login_required(login_url=common.views.login_view)
def admins_student_detail_view(request,*args,**kwargs):
    return render(request,"admins/students.html")

#for edit add
@login_required(login_url=common.views.login_view)
def admins_student_edit(request,account_id):
    print(account_id)
    displaydata=Student.objects.get(account_id=account_id)
    print(displaydata)
    return render(request,'admins/edit.html',{'editdata':displaydata})

@login_required(login_url=common.views.login_view)
def edit_student(request,account_id):
    updatedata=Student.objects.get(account_id=account_id)
    form=forms.editforms()
    print(account_id)
    if request.method=='POST':
        print('post')
    if request.method == "POST":
        form=editforms(request.POST or None,instance=updatedata)
        #error here
        if form.is_valid():
            form.save()
            messages.success(request,"record updated")
            return render(request,'admins/edit.html',{'editdata':updatedata})
        else:
            return HttpResponse(messages)
    print(form.errors)

@login_required(login_url=common.views.login_view)
def logout_view(request, *args, **kwargs):
    logout(request)
    # form = LoginForm(request.post or None)
    # context = {
    #     'form':form,
    # }
    return redirect(common.views.login_view)


   
    
    