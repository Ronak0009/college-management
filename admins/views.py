from django.shortcuts import render
from students.models import Student
from admins.forms import editforms
from django.contrib import messages
from django.http import HttpResponse
from  . import forms


# Create your views here.

def admins_home_view(request, *args, **kwargs):
    return render(request, "admins/home.html")

def admins_courses_view(request, *args, **kwargs):
    return render(request, "admins/courses.html")

def admins_students_view(request, *args, **kwargs):
    return render(request, "admins/students.html")

def admins_staff_view(request, *args, **kwargs):
    return render(request, "admins/staff.html")

def admins_profile_view(request, *args, **kwargs):
    return render(request, "admins/profile.html")

# for data extraction
def admins_student_pending_detail_view(request,*args,**kwargs):
    obj=Student.objects.filter(isPending=True)
    print(obj)
    return render(request,"admins/students.html",{'student':obj})

def admins_student_detail_view(request,*args,**kwargs):
    return render(request,"admins/students.html")

#for edit add
def admins_student_edit(request,account_id):
    print(account_id)
    displaydata=Student.objects.get(account_id=account_id)
    print(displaydata)
    return render(request,'admins/edit.html',{'editdata':displaydata})

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



   
    
    