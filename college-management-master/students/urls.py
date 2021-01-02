from django.urls import path
from .views import *

app_name = 'students'
urlpatterns = [
    path('home/', student_home_view, name="home"),
    path('courses/',student_courses_view, name="courses"),
    path('results/',student_results_view, name="results"),
    path('attendance/',student_attendance_view, name="attendance"),
    path('profile/',student_profile_view, name="profile")
]