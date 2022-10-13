from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='superhome'),
    path('busadminregister/', views.BusRegisterPage, name='busregister'),
    path('trainadminregister/', views.TrainRegisterPage, name='trainregister'),
]