from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path("postcomment",views.postComment,name='postComment'),
    path('posts', views.latestpost, name="posts"),
    path('<str:slug>', views.blogpost, name="blogpost"),
    
]