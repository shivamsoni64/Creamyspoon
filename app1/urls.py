from django.contrib import admin
from django.urls import path
from app1 import views
urlpatterns = [
                 path("", views.index, name='home'),
                 path("varieties", views.varieties, name='varieties'),
                 path("blogs", views.blogs, name='blogs'),
                 path("knowus", views.knowus, name='knowus'),
                 path("contactus", views.contactus, name='contactus')

]