from django.shortcuts import render

# Create your views here.

def student_home_view(request, *args, **kwargs):
    return render(request, "students/home.html")