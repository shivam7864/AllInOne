from django.contrib import admin
from django.urls import path,include
from  .import views

urlpatterns = [
    
    path('', views.index,name="index"),
    path('countrywise', views.countrywise,name="countrywise"),
    path('search', views.search,name="search"),
    
]