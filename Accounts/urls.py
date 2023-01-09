from django.urls import path
from Accounts.views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('singup/', signup, name='singup'),
    path('login/', login_request, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', editProfile, name= "singEditForm"),
    path('profileAvatar/', addAvatar, name= "addAvatar"),

]

