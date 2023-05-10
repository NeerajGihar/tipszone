from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path("postcomment",views.postComment,name='postComment'),
    path('<str:slug>', views.blogpost, name="blogpost"),
]