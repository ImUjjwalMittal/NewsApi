from django.contrib import admin
from django.conf.urls import url 
from django.urls import path , include 
from  . import views 

urlpatterns = [
    path('stats/' , views.index , name = 'index'),
]

   
