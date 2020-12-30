from django.shortcuts import render

# Create your views here.

def login_view(request, *args, **kwargs):
    return render(request, "common/home.html")

def student_registration(request,*args,**kwargs):
    return render(request,"common/studentreg.html")

def staff_registration(request,*args,**kwargs):
    return render(request,"common/staffreg.html")