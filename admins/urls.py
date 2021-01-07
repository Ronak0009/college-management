from django.urls import path
from .views import *

app_name = 'college-admin'
urlpatterns = [
    path('home/', admins_home_view, name="home"),
    path('students/', admins_students_view, name="students"),
    path('staff/', admins_staff_view, name="staff"),
    path('courses/', admins_courses_view, name="courses"),
    path('profile/', admins_profile_view, name="profile"),

    #new
    path('student-account-pending-details/',admins_student_pending_detail_view,name='studentsdetails'),
    path('student-account-details/',admins_student_detail_view,name='studentsdetails2'),

    #for edit
    path('edit/<int:account_id>',admins_student_edit,name='studentedit'),
    path('update/<int:account_id>/',edit_student,name='studentupdate'),

]