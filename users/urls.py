from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage),
    path('login/', views.loginPage),
    path('register/', views.registerPage),
    path('test/', views.testPage)
]