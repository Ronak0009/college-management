from django.shortcuts import render

# Create your views here.

def staff_home_view(request, *args, **kwargs):
    return render(request, "staff/home.html")