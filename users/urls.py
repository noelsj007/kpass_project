from django.views.generic import TemplateView
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('dashboard/', views.dashPage, name='dash'),
    path('notfound/', views.notfoundPage, name='notfound'),
    path('profile/', views.UserProfilePage, name='profile'),
    path('test/', views.TestPage, name='test'),
    path('buspassform/', views.BusPassForm, name='buspassform'),
    path('trainpassform/', views.TrainPassForm, name='trainpassform'),
    path('buspassapplication/', views.view_pass_forms, name='buspassapplication'),
    path('buspassview/', views.busPassView, name='buspassview'),
    path('<int:pass_id>/busvirtualpassview/', views.busVirtualPassView, name='busvirtualpassview'),
    # path('payment/<int:amount>/', views.payment, name='payment'),
    path('<int:pass_id>/razorpay_payment/', views.razorpay_payment, name='razorpay_payment'),
    path('<int:pass_id>/verify/', views.verifyBusPass, name='verifybuspass')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)