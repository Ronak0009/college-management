from django.urls import path
from .views import *

app_name = 'college-admin'
urlpatterns = [
    path('home/', admin_home_view, name="home")
]