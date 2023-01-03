from django.urls import path
from Accounts.views import *

urlpatterns = [
    path('singup/', singup, name='singup'),
    
]
