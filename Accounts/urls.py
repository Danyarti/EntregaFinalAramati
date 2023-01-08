from django.urls import path
from Accounts.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('singup/', signup, name='singup'),
    path('login/', login_request, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
