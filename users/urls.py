from django.views.generic import TemplateView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('dashboard/', views.dashPage, name='dash'),
    path('notfound/', views.notfoundPage, name='notfound'),
    path('profile/', views.UserProfilePage, name='profile'),
    path('test/', views.TestPage, name='test')

]