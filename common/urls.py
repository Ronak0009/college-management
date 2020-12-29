from django.urls import path
from .views import *

app_name = ''
urlpatterns = [
    path('login/', login_view, name="login")
]