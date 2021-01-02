from django.shortcuts import render

# Create your views here.

def staff_home_view(request, *args, **kwargs):
    return render(request, "staff/home.html")

def staff_courses_view(request, *args, **kwargs):
    return render(request, "staff/courses.html")

def staff_attendance_view(request, *args, **kwargs):
    return render(request, "staff/attendance.html")

def staff_results_view(request, *args, **kwargs):
    return render(request, "staff/results.html")

def staff_profile_view(request, *args, **kwargs):
    return render(request, "staff/profile.html")