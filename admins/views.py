from django.shortcuts import render

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