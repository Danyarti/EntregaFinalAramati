from django.urls import path
from Blog.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index), 
    path('review/', blogForm, name="blogForm"),
    path('allBlogs/', allBlogs , name="allBlogs"),
    path('blog/<id>', blogPost , name="blogPost"),
    path('editBlog/<id>', editBlog , name="editBlog"),
    path('userPost', userPosts, name="userPosts"),
    path('deletePost/<id>', deletePost, name="deletePost"),
]

