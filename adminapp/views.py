from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.template import ContextPopException
from .forms import UserAdminCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .superdecorator import *
from users import models as Users

# Create your views here.

@login_required(login_url='login')
@allowed_users(allowed_roles=['SuperAdmin'])
def homePage(request):

    
    admin_count = Users.CustomUser.objects.filter(groups__name__in=['TrainAdmin', 'BusAdmin', 'SuperAdmin']).count()
    user_count = Users.CustomUser.objects.filter(groups__name__in = ['customer']).count()

    print(admin_count, user_count)
    context={'admin_count': admin_count, 'user_count': user_count}

    return render(request, 'adminhome.html', context )


@allowed_users(allowed_roles=['SuperAdmin'])
def BusAdminPage(request):
    bus_user = Users.CustomUser.objects.filter(groups__name__in=['BusAdmin'])



    context = {'bus_user': bus_user}

    return render(request, 'bussystemuser.html', context)

@allowed_users(allowed_roles=['SuperAdmin'])
def TrainAdminPage(request):
    train_user = Users.CustomUser.objects.filter(groups__name__in=['TrainAdmin'])



    context = {'train_user': train_user}
    return render(request, 'trainsystemuser.html', context)



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