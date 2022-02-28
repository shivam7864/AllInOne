from django.contrib import admin
from django.urls import path,include
from  .import views

urlpatterns = [
    
    path('', views.index,name="index"),
    path('globalnews', views.globalnews,name="globalnews"),
    path('business', views.business,name="business"),
    path('entertainment', views.entertainment,name="entertainment"),
    path('bitcoin', views.bitcoin,name="bitcoin"),
    path('sports', views.sports,name="sports"),
    
    
]