from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.template import ContextPopException
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .superdecorator import *
from users import models as Users
from ksrtc import models as ksrtc
from irctc import models as irctc
from irctc import forms as trainform

# Create your views here.

@login_required(login_url='login')
@allowed_users(allowed_roles=['SuperAdmin'])
def homePage(request):

    
    admin_count = Users.CustomUser.objects.filter(groups__name__in=['TrainAdmin', 'BusAdmin', 'SuperAdmin']).count()
    user_count = Users.CustomUser.objects.filter(groups__name__in = ['customer']).count()

    print(admin_count, user_count)
    context={'admin_count': admin_count, 'user_count': user_count}

    return render(request, 'adminhome.html', context )

#Bus

@allowed_users(allowed_roles=['SuperAdmin'])
def BusAdminPage(request):
    bus_user = Users.CustomUser.objects.filter(groups__name__in=['BusAdmin'])



    context = {'bus_user': bus_user}

    return render(request, 'bussystemuser.html', context)


@allowed_users(allowed_roles=['SuperAdmin'])
def BusPlacePage(request):
    bus_place_details = ksrtc.Place.objects.all()
    bus_place_details_pk = bus_place_details[0].id



    context = {'bus_place_details': bus_place_details, 'bus_place_details_pk':bus_place_details_pk}
    return render(request, 'busplace.html', context)

@allowed_users(allowed_roles=['SuperAdmin'])
def BusRoutePage(request):
    bus_route_details = ksrtc.BusRoute.objects.all()
    bus_route_details_pk = bus_route_details[0].id



    context = {'bus_route_details': bus_route_details, 'bus_route_details_pk':bus_route_details_pk}
    return render(request, 'busroute.html', context)


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


def BusPlaceRegister(request):
    form = KstrcPlaceForms()
    if request.method == 'POST':
        form = KstrcPlaceForms(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect('busplace')
    return render(request, 'busplaceregister.html', {'form': form})

def BusPlaceEditPage(request, pk):

    bus_place_details = ksrtc.Place.objects.get(id=pk)
    form = KstrcPlaceForms(instance=bus_place_details)
    if request.method == 'POST':
        form = KstrcPlaceForms(request.POST, instance=bus_place_details)
        if form.is_valid():
            form.save()

        return redirect('busplace')

    return render(request, 'busplaceregister.html', {'form': form})


def BusEditPage(request, pk):
    admin_detail = Users.CustomUser.objects.get(id=pk)
    form = UserAdminCreationForm(instance=admin_detail)
    if request.method =='POST':
        form = UserAdminCreationForm(request.POST, instance = admin_detail)
        if form.is_valid():
            form.save()

        return redirect('superhome')

    return render(request, 'adminedit.html', {'form': form} )

def DeleteBusAdmin(request, pk):
    bus_admin_detail = Users.CustomUser.objects.get(id=pk)
    bus_admin_detail.delete()
    return redirect('busadminr')


def DeleteSchool(request, pk):
    school_details = SchoolDetail.objects.get(id=pk)
    school_details.delete()
    return redirect('school')

def DeleteBusPlace(request, pk):
    school_details = ksrtc.Place.objects.get(id=pk)
    school_details.delete()
    return redirect('busplace')

def BusSubTimes(request):
    bus_sub_time = ksrtc.SubTime.objects.all()
    bus_sub_time_pk = bus_sub_time[0].id



    context = {'bus_sub_time': bus_sub_time, 'bus_sub_time_pk':bus_sub_time_pk}
    return render(request, 'bustime.html', context)

def BusTimeRegister(request):
    form = KsrtcSubTimeForm()
    if request.method == 'POST':
        form = KsrtcSubTimeForm(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect('bustime')
    return render(request, 'traintimeregister.html', {'form': form})

def BusTimeEditPage(request, pk):

    bus_time_details = ksrtc.SubTime.objects.get(id=pk)
    form = KsrtcSubTimeForm(instance=bus_time_details)
    if request.method == 'POST':
        form = KsrtcSubTimeForm(request.POST, instance=bus_time_details)
        if form.is_valid():
            form.save()

        return redirect('bustime')

    return render(request, 'bustimeregister.html', {'form': form})

def DeleteBusTime(request, pk):
    school_details = ksrtc.SubTime.objects.get(id=pk)
    school_details.delete()
    return redirect('bustime')

#School


@allowed_users(allowed_roles=['SuperAdmin'])
def SchoolPage(request):
    school_details = SchoolDetail.objects.all()
    school_details_pk = school_details[0].id



    context = {'school_details': school_details, 'school_details_pk':school_details_pk}
    return render(request, 'busschool.html', context)


def SchoolEditPage(request, pk):

    school_details = SchoolDetail.objects.get(id=pk)
    form = SchoolDetailForm(instance=school_details)
    if request.method == 'POST':
        form = SchoolDetailForm(request.POST, instance=school_details)
        if form.is_valid():
            form.save()

        return redirect('superhome')

    return render(request, 'schoolregister.html', {'form': form})



def SchoolRegisterPage(request):
    form = SchoolDetailForm()
    if request.method == 'POST':
        form = SchoolDetailForm(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect('school')
    return render(request, 'schoolregister.html', {'form': form})


#Train

def TrainPlaceRegister(request):
    form = IrctcPlaceForms()
    if request.method == 'POST':
        form = IrctcPlaceForms(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect('trainplace')
    return render(request, 'trainplaceregister.html', {'form': form})


def TrainPlaceEditPage(request, pk):

    train_place_details = irctc.TrainPlace.objects.get(id=pk)
    form = IrctcPlaceForms(instance=train_place_details)
    if request.method == 'POST':
        form = IrctcPlaceForms(request.POST, instance=train_place_details)
        if form.is_valid():
            form.save()

        return redirect('trainplace')

    return render(request, 'trainplaceregister.html', {'form': form})


@allowed_users(allowed_roles=['SuperAdmin'])
def TrainPlacePage(request):
    train_place_details = irctc.TrainPlace.objects.all()
    train_place_details_pk = train_place_details[0].id



    context = {'train_place_details': train_place_details, 'train_place_details_pk':train_place_details_pk}
    return render(request, 'trainplace.html', context)

def DeleteTrainPlace(request, pk):
    school_details = irctc.TrainPlace.objects.get(id=pk)
    school_details.delete()
    return redirect('trainplace')

@allowed_users(allowed_roles=['SuperAdmin'])
def TrainAdminPage(request):
    train_user = Users.CustomUser.objects.filter(groups__name__in=['TrainAdmin'])



    context = {'train_user': train_user}
    return render(request, 'trainsystemuser.html', context)


@allowed_users(allowed_roles=['SuperAdmin'])
def TrainRegisterPage(request):

    form = UserAdminCreationForm()
    if request.method == 'POST':
        form = UserAdminCreationForm(request.POST)
        if form.is_valid():
            user = form.save()


            group = Group.objects.get(name='TrainAdmin') 
            user.groups.add(group)

        return redirect('trainadminr')
    return render(request, 'adminregister.html', {'form': form})


def TrainEditPage(request, pk):
    admin_detail = Users.CustomUser.objects.get(id=pk)
    form = UserAdminCreationForm(instance=admin_detail)
    if request.method =='POST':
        form = UserAdminCreationForm(request.POST, instance = admin_detail)
        if form.is_valid():
            form.save()

        return redirect('superhome')

    return render(request, 'adminedit.html', {'form': form} )

def DeleteTrainAdmin(request, pk):
    bus_admin_detail = Users.CustomUser.objects.get(id=pk)
    bus_admin_detail.delete()
    return redirect('trainadminr')

@allowed_users(allowed_roles=['SuperAdmin'])
def TrainRoutePage(request):
    train_route_details = irctc.TrainRoute.objects.all()
    train_route_details_pk = train_route_details[0].id



    context = {'train_route_details': train_route_details, 'train_route_details_pk':train_route_details_pk}
    return render(request, 'trainroute.html', context)


def TrainSubTimes(request):
    train_sub_time = irctc.TrainSubTime.objects.all()
    train_sub_time_pk = train_sub_time[0].id



    context = {'train_sub_time': train_sub_time, 'train_sub_time_pk':train_sub_time_pk}
    return render(request, 'traintime.html', context)


def TrainRouteRegister(request):
    form = TrainRouteForm()
    if request.method == 'POST':
        form = TrainRouteForm(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect('trainplace')
    return render(request, 'trainrouteregister.html', {'form': form})

def TrainTimeRegister(request):
    form = IrctcSubTimeForm()
    if request.method == 'POST':
        form = IrctcSubTimeForm(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect('traintime')
    return render(request, 'traintimeregister.html', {'form': form})

def TrainTimeEditPage(request, pk):

    train_time_details = irctc.TrainSubTime.objects.get(id=pk)
    form = IrctcSubTimeForm(instance=train_time_details)
    if request.method == 'POST':
        form = IrctcSubTimeForm(request.POST, instance=train_time_details)
        if form.is_valid():
            form.save()

        return redirect('traintime')

    return render(request, 'traintimeregister.html', {'form': form})

def TrainRouteEditPage(request, pk):

    train_place_details = irctc.TrainRoute.objects.get(id=pk)
    form = TrainRouteForm(instance=train_place_details)
    if request.method == 'POST':
        form = TrainRouteForm(request.POST, instance=train_place_details)
        if form.is_valid():
            form.save()

        return redirect('trainroute')

    return render(request, 'trainrouteregister.html', {'form': form})


def DeleteTrainRoute(request, pk):
    school_details = irctc.TrainPlace.objects.get(id=pk)
    school_details.delete()
    return redirect('trainroute')

def DeleteTrainTime(request, pk):
    school_details = irctc.TrainRoute.objects.get(id=pk)
    school_details.delete()
    return redirect('traintime')



    