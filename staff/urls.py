from django.urls import path
from .views import *

app_name = 'staff'
urlpatterns = [
    path('home/', staff_home_view, name="home"),
    path('courses/',staff_courses_view, name="courses"),
    path('results/',staff_results_view, name="results"),
    path('attendance/',staff_attendance_view, name="attendance"),
    path('profile/',staff_profile_view, name="profile")
]