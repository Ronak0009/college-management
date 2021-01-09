from django.shortcuts import render, redirect
from students.models import Student
from admins.forms import editforms
from admins.forms1 import editforms1
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import common
from staff.models import Staff
from  . import forms
from datetime import datetime
from common.forms import LoginForm


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
# admin profile edit
def admins_profile_view(request, *args, **kwargs):
    obj=Staff.objects.filter(isAdmin=True)
    print(obj)
    return render(request, "admins/profile.html",{'admin':obj})

def admins_profile_edit(request,account_id):
    print(account_id)
    displaydata=Staff.objects.get(account_id=account_id)
    print(displaydata)
    return render(request,'admins/adminprofileedit.html',{'editdata':displaydata})

def edit_profile(request,account_id):
    updatedata=Staff.objects.get(account_id=account_id)
    print(account_id)
    if request.method == "POST":
        print('post')
        form=editforms1(request.POST or None,instance=updatedata)
        #error here
        if form.is_valid():
            form.save()
            messages.success(request,"Your Profile updated")
            return render(request,'admins/adminprofileedit.html',{'editdata':updatedata})
        else:
            return HttpResponse(messages)
    print(form.errors)

# for data extraction for student
@login_required(login_url=common.views.login_view)
def admins_student_pending_detail_view(request,*args,**kwargs):
    obj=Student.objects.filter(isPending=True)
    print(obj)
    return render(request,"admins/students.html",{'student':obj})
    
# load approved acounts    
def admins_student_approved_detail_view(request,*args,**kwargs):
    obj=Student.objects.filter(isPending=False)
    return render(request,"admins/studentapproved.html",{'student':obj})

#for edit page will be called to edit approved accounts
def admins_student_approve(request,account_id):
    print(account_id)
    displaydata=Student.objects.get(account_id=account_id)
    print(displaydata)
    return render(request,'admins/studentapprove.html',{'editdata':displaydata})

#edit approved details will be validated
def approve_student(request,account_id):
    updatedata=Student.objects.get(account_id=account_id)
    print(account_id)
    if request.method == "POST":
        print('post')
        form=editforms(request.POST or None,instance=updatedata)
        #error here
        if form.is_valid():
            form.save()
            messages.success(request,"Student Approved")
            return render(request,'admins/studentapprove.html',{'editdata':updatedata})
        else:
            return HttpResponse(messages)
    print(form.errors)

#edit page will be called for unapproved details of students

@login_required(login_url=common.views.login_view)
def admins_student_detail_view(request,*args,**kwargs):
    return render(request,"admins/students.html")
  
@login_required(login_url=common.views.login_view)
def admins_student_edit(request,account_id):
    print(account_id)
    displaydata=Student.objects.get(account_id=account_id)
    print(displaydata)
    return render(request,'admins/studentedit.html',{'editdata':displaydata})

#to edit unapproved students
@login_required(login_url=common.views.login_view)
def edit_student(request,account_id):
    updatedata=Student.objects.get(account_id=account_id)
    print(account_id)
    if request.method == "POST":
        print('post')
        form=editforms(request.POST or None,instance=updatedata)
        #error here
        if form.is_valid():
            form.save()
            messages.success(request,"student data updated")
            return render(request,'admins/studentedit.html',{'editdata':updatedata})
        else:
            return HttpResponse(messages)
    print(form.errors)



#for extraction of staff

def admins_staff_pending_detail_view(request,*args,**kwargs):
    obj=Staff.objects.filter(isPending=True)
    print(obj)
    return render(request,"admins/staff.html",{'staff':obj})

def admins_staff_approved_detail_view(request,*args,**kwargs):
    obj=Staff.objects.filter(isPending=False)
    return render(request,"admins/staffapproved.html",{'staff':obj})

#for edit add
def admins_staff_approve(request,account_id):
    print(account_id)
    displaydata=Staff.objects.get(account_id=account_id)
    print(displaydata)
    return render(request,'admins/staffapprove.html',{'editdata':displaydata})

def approve_staff(request,account_id):
    updatedata=Staff.objects.get(account_id=account_id)
    print(account_id)
    if request.method == "POST":
        print('post')
        form=editforms1(request.POST or None,instance=updatedata)
        #error here
        if form.is_valid():
            form.save()
            messages.success(request,"Staff Member Approved")
            return render(request,'admins/staffapprove.html',{'editdata':updatedata})
        else:
            return HttpResponse(messages)
    print(form.errors)


def admins_staff_edit(request,account_id):
    print(account_id)
    displaydata=Staff.objects.get(account_id=account_id)
    print(displaydata)
    return render(request,'admins/staffedit.html',{'editdata':displaydata})

def edit_staff(request,account_id):
    updatedata=Staff.objects.get(account_id=account_id)
    print(account_id)
    if request.method == "POST":
        print('post')
        form=editforms1(request.POST or None,instance=updatedata)
        #error here
        if form.is_valid():
            form.save()
            messages.success(request,"Staff Member data updated")
            return render(request,'admins/staffedit.html',{'editdata':updatedata})
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


   
    
    