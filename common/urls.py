from django.urls import path
from .views import *

app_name = ''
urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', registration_view, name="register"),
    path('student-registration/',student_registration, name="student"),
    path('staff-registration/', staff_registration, name="staff"),
    path('pending-account/', pending_account_view, name="pending-account"),
    path('account-created/', account_created_view, name="account-created"),
]