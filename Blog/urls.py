from django.urls import path
from Blog.views import *


urlpatterns = [
    path('', index), 
    path('review/', blogForm, name="blogForm"),   
]