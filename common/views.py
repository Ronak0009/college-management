from django.shortcuts import render
from students.forms import StudentForm
from staff.forms import StaffForm

# Create your views here.

def login_view(request, *args, **kwargs):
    return render(request, "common/home.html")

def student_registration(request,*args,**kwargs):
    f=StudentForm()
    return render(request,"common/studentregistration.html",{'form':f})

def staff_registration(request,*args,**kwargs):
    f=StaffForm()
    return render(request,"common/staffregistration.html",{'form':f})