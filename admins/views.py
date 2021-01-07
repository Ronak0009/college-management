from django.shortcuts import render
from students.models import Student
from datetime import datetime

# Create your views here.

def admins_home_view(request, *args, **kwargs):
    time = datetime.now()
    currentTime = time.strftime("%D %I:%M:%S %p")
    context = {
        'timestamp': currentTime,
    }
    return render(request, "admins/home.html",context)

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
    return render(request,"admins/students.html",{'student':obj})

def admins_student_detail_view(request,*args,**kwargs):
    return render(request,"admins/students.html")
   
    
    