from django.shortcuts import render

# Create your views here.

def admin_home_view(request, *args, **kwargs):
    return render(request, "admins/home.html")