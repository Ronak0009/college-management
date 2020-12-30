from django.urls import path
from .views import *

app_name = 'students'
urlpatterns = [
    path('home/', student_home_view, name="home")
]