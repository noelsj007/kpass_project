from django.shortcuts import render
from .traindecorator import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
@allowed_users(allowed_roles=['TrainAdmin'])
def homePage(request):
    return render(request, 'trainhome.html')