"""blogsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .import views
from home import views1
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header="TipZone Admin"
admin.site.site_title="TipZone Admin Panel"
admin.site.index_title="Welcome to TipZone Admin Panel"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name="index"),
    path('contact/',views1.Contact,name="Contact"),
    path('about/',views1.about, name="about"),
    path('search',views1.search, name="search"),
    path('signup',views1.SignUp, name="SignUp"),
    path('login',views1.LogIn, name="LogIn"),
    path('logout',views1.LogOut, name="LogOut"),
    path('blog/', include('blog.urls')),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
