from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    # path('speak', views.speak, name="speak"),
    
]
