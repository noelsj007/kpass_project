from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='superhome'),
    path('busadminregister/', views.BusRegisterPage, name='busregister'),
    path('trainadminregister/', views.TrainRegisterPage, name='trainregister'),
    path('busadmindetails/', views.BusAdminPage, name='busadminr'),
    path('trainadmindetails/', views.TrainAdminPage, name='trainadminr'),
    path('schoolregister/', views.SchoolRegisterPage, name='schoolregister'),
    path('school/', views.SchoolPage, name='school'),
    path('schooledit/<str:pk>/', views.SchoolEditPage, name='schooledit'),
    path('trainedit/<str:pk>/', views.TrainEditPage, name='trainedit'),
    path('busedit/<str:pk>/', views.BusEditPage, name='busedit'),
    path('deletebus/<str:pk>/', views.DeleteBusAdmin, name='deletebus'),
    path('deletetrain/<str:pk>/', views.DeleteTrainAdmin, name='deletetrain'),
    path('deleteschool/<str:pk>/', views.DeleteSchool, name='deleteschool'),
]