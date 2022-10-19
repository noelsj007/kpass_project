from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='superhome'),
    path('busadminregister/', views.BusRegisterPage, name='busregister'),
    path('trainadminregister/', views.TrainRegisterPage, name='trainregister'),
    path('userregister/', views.UserRegisterPage, name='userregister'),
    path('busadmindetails/', views.BusAdminPage, name='busadminr'),
    path('trainadmindetails/', views.TrainAdminPage, name='trainadminr'),
]