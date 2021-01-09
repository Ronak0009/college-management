from django.urls import path
from .views import *

app_name = 'college-admin'
urlpatterns = [
    path('home/', admins_home_view, name="home"),
    path('students/', admins_students_view, name="students"),
    path('staff/', admins_staff_view, name="staff"),
    path('courses/', admins_courses_view, name="courses"),
    path('profile/', admins_profile_view, name="profile"),

    #student
    path('student-account-pending-details/',admins_student_pending_detail_view,name='studentsdetails'),
    path('student-account-approved-details/',admins_student_approved_detail_view,name='studentsdetails2'),

    #for edit
    path('approve-student/<int:account_id>',admins_student_approve,name='studentapprove'),
    path('approved-student/<int:account_id>/',approve_student,name='studentapproved'),

    path('edit-student/<int:account_id>',admins_student_edit,name='studentedit'),
    path('update-student/<int:account_id>/',edit_student,name='studentupdate'),


    #for staff
    path('staff-account-pending-details/',admins_staff_pending_detail_view,name='staffdetails'),
    path('staff-account-approved-details/',admins_staff_approved_detail_view,name='staffdetails2'),

    #for edit
    path('approve-staff/<int:account_id>',admins_staff_approve,name='staffapprove'),
    path('approved-staff/<int:account_id>/',approve_staff,name='staffapproved'),

    path('edit-staff/<int:account_id>',admins_staff_edit,name='staffedit'),
    path('update-staff/<int:account_id>/',edit_staff,name='staffupdate'),


    # for admin profile edit
    path('edit-profile/<int:account_id>',admins_profile_edit,name='adminedit'),
    path('update-profile/<int:account_id>/',edit_profile,name='adminupdate'),


]