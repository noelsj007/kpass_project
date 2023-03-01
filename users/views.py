from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserAdminCreationForm, KsrtcPassFormField
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorator import *
from .models import *

# Create your views here.

# @login_required(login_url='login')
def homePage(request):
    return render(request, 'home.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])

def dashPage(request):
    return render(request, 'userdashboard.html')

def UserProfilePage(request):

    return render (request, 'profile.html')

def notfoundPage(request):
    return render(request, '404.html')


def TestPage(request):
    return render(request, 'test.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

@unauthenticated_user
def loginPage(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('dash')
        
        else:
            messages.info(request, 'Password Or Username is incorrect')
            

    return render(request, 'login.html')

# def registerPage(request):
#     form = UserCreationForm()
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#     context = {'form': form}
#     return render(request, 'register.html', context)


@unauthenticated_user
def registerPage(request):

    form = UserAdminCreationForm()
    if request.method == 'POST':
        form = UserAdminCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('first_name')


            group = Group.objects.get(name='customer') 
            user.groups.add(group)


            messages.success(request, 'Account Created for ' + str(user) + ' Please login')
            return redirect('login')
    return render(request, 'userregister.html', {'form': form})


def BusPassForm(request):
    form = KsrtcPassFormField()
    if request.method=='POST':
        form = KsrtcPassFormField(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'buspassform.html', {'form':form})

def TrainPassForm(request):
    return render(request, 'trainpassform.html')