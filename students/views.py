from django.shortcuts import render

# Create your views here.

def student_home_view(request, *args, **kwargs):
    return render(request, "students/home.html")

def student_courses_view(request, *args, **kwargs):
    return render(request, "students/courses.html")

def student_attendance_view(request, *args, **kwargs):
    return render(request, "students/attendance.html")

def student_results_view(request, *args, **kwargs):
    return render(request, "students/results.html")

def student_profile_view(request, *args, **kwargs):
    return render(request, "students/profile.html")