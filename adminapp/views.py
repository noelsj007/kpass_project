from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserAdminCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .superdecorator import *

# Create your views here.

@login_required(login_url='login')
@allowed_users(allowed_roles=['SuperAdmin'])
def homePage(request):
    return render(request, 'adminhome.html')


@allowed_users(allowed_roles=['SuperAdmin'])
def BusRegisterPage(request):

    form = UserAdminCreationForm()
    if request.method == 'POST':
        form = UserAdminCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('first_name')


            group = Group.objects.get(name='BusAdmin') 
            user.groups.add(group)


            # messages.success(request, 'Account Created for ' + user + ' Please login')
            return redirect('superhome')
    return render(request, 'adminregister.html', {'form': form})


@allowed_users(allowed_roles=['SuperAdmin'])
def TrainRegisterPage(request):

    form = UserAdminCreationForm()
    if request.method == 'POST':
        form = UserAdminCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('first_name')


            group = Group.objects.get(name='TrainAdmin') 
            user.groups.add(group)

            


            # messages.success(request, 'Account Created for ' + user + ' Please login')
            return redirect('superhome')
    return render(request, 'adminregister.html', {'form': form})

def UserRegisterPage(request):

    form = UserAdminCreationForm()
    if request.method == 'POST':
        form = UserAdminCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('first_name')


            group = Group.objects.get(name='customer') 
            user.groups.add(group)


            # messages.success(request, 'Account Created for ' + user + ' Please login')
            return redirect('superhome')
    return render(request, 'userregister.html', {'form': form})