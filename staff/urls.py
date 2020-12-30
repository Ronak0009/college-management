from django.urls import path
from .views import *

app_name = 'staff'
urlpatterns = [
    path('home', staff_home_view, name="home")
]