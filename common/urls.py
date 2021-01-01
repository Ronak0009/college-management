from django.urls import path
from .views import *

app_name = ''
urlpatterns = [
    path('login/', login_view, name="login"),
    path('student-registration/',student_registration, name="student"),
    path('staff-registration/', staff_registration, name="staff"),
    path('admin-login/',admin_login,name="adminlogin")

]