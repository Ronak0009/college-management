from django.shortcuts import render, get_object_or_404, redirect
from students.forms import StudentForm
from staff.forms import StaffForm
from students.models import Student

# Create your views here.

def login_view(request, *args, **kwargs):
    return render(request, "common/home.html")

def admin_login(request,*args,**kwargs):
    return render(request,"admins/home.html")

def registration_view(request,*args,**kwargs):
    return render(request,"common/register.html")

def student_registration(request,*args,**kwargs):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Student.objects.create(**form.cleaned_data)
            return redirect("../login")

    return render(request,"common/studentregistration.html",{'form':form})

def staff_registration(request,*args,**kwargs):
    f=StaffForm()
    return render(request,"common/staffregistration.html",{'form':f})

