from django.shortcuts import render
from .busdecorators import *
from django.contrib.auth.decorators import login_required
from adminapp.models import *
from adminapp.forms import *
from . import models as ksrtc
from django.db.models import Sum
from .forms import *


# Create your views here.

@login_required(login_url='login')
@bus_allowed_users(allowed_roles=['BusAdmin', 'SuperAdmin'])
def homePage(request):
    total_bus_value = PassForm.objects.aggregate(total=Sum('amount'))['total']
    # total_train_value = TrainStudentPassForm.objects.aggregate(total=Sum('amount'))['total']
    total_payment =(total_bus_value or 0)
    # unpaid_train_pass_form = PassForm.objects.filter(paid=False).count()
    unpaid_pass_form_count = PassForm.objects.filter(paid=False).count()
    total_pending_pass =unpaid_pass_form_count
    pass_form_count = PassForm.objects.filter(paid=True).count()
    pass_forms= PassForm.objects.filter(paid=True).order_by('-id')[:4]
    train_pass_count = (pass_form_count)
    total_routes = BusRoute.objects.all().count()
    bus_routes = BusRoute.objects.all()
    # print(train_pass_count)

    context={
        'total_payment' : total_payment,
        'total_pending_pass' : total_pending_pass,
        'pass_forms' : pass_forms,
        'train_pass_count' : train_pass_count,
        'total_routes' : total_routes,
        'bus_routes' : bus_routes,
        }
    return render(request, 'bushome.html', context)



def BPassPage(request):
    bpass_details = ksrtc.PassForm.objects.all()



    context = {'bpass_details': bpass_details}
    return render(request, 'bbpass.html', context)


def BPassEditPage(request, pk):

    bpass_details = ksrtc.PassForm.objects.get(id=pk)
    form = KsrtcPassFormField(instance=bpass_details)
    if request.method == 'POST':
        form = KsrtcPassFormField(request.POST, instance=bpass_details)
        if form.is_valid():
            form.save()

        return redirect('btpass')

    return render(request, 'bbpassregister.html', {'form': form})

def DeleteBPass(request, pk):
    bpass_details = ksrtc.PassForm.objects.get(id=pk)
    bpass_details.delete()
    return redirect('btpass')

@bus_allowed_users(allowed_roles=['BusAdmin', 'SuperAdmin'])
def BusPlacePage(request):
    bus_place_details = ksrtc.Place.objects.all()
    bus_place_details_pk = bus_place_details[0].id



    context = {'bus_place_details': bus_place_details, 'bus_place_details_pk':bus_place_details_pk}
    return render(request, 'bbusplace.html', context)

@bus_allowed_users(allowed_roles=['BusAdmin','SuperAdmin'])
def BusRoutePage(request):
    bus_route_details = ksrtc.BusRoute.objects.all()
    bus_route_details_pk = bus_route_details[0].id



    context = {'bus_route_details': bus_route_details, 'bus_route_details_pk':bus_route_details_pk}
    return render(request, 'bbusroute.html', context)



def BusPlaceRegister(request):
    form = KstrcPlaceForms()
    if request.method == 'POST':
        form = KstrcPlaceForms(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect('bbusplace')
    return render(request, 'bbusplaceregister.html', {'form': form})

def BusPlaceEditPage(request, pk):

    bus_place_details = ksrtc.Place.objects.get(id=pk)
    form = KstrcPlaceForms(instance=bus_place_details)
    if request.method == 'POST':
        form = KstrcPlaceForms(request.POST, instance=bus_place_details)
        if form.is_valid():
            form.save()

        return redirect('bbusplace')

    return render(request, 'bbusplaceregister.html', {'form': form})




def DeleteSchool(request, pk):
    school_details = SchoolDetail.objects.get(id=pk)
    school_details.delete()
    return redirect('bschool')

def DeleteBusPlace(request, pk):
    school_details = ksrtc.Place.objects.get(id=pk)
    school_details.delete()
    return redirect('bbusplace')

def BusSubTimes(request):
    bus_sub_time = ksrtc.SubTime.objects.all()
    bus_sub_time_pk = bus_sub_time[0].id



    context = {'bus_sub_time': bus_sub_time, 'bus_sub_time_pk':bus_sub_time_pk}
    return render(request, 'bbustime.html', context)

def BusTimeRegister(request):
    form = KsrtcSubTimeForm()
    if request.method == 'POST':
        form = KsrtcSubTimeForm(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect('bbustime')
    return render(request, 'bustimeregister.html', {'form': form})

def BusTimeEditPage(request, pk):

    bus_time_details = ksrtc.SubTime.objects.get(id=pk)
    form = KsrtcSubTimeForm(instance=bus_time_details)
    if request.method == 'POST':
        form = KsrtcSubTimeForm(request.POST, instance=bus_time_details)
        if form.is_valid():
            form.save()

        return redirect('bbustime')

    return render(request, 'bustimeregister.html', {'form': form})

def DeleteBusTime(request, pk):
    school_details = ksrtc.SubTime.objects.get(id=pk)
    school_details.delete()
    return redirect('bbustime')

    

#School


@bus_allowed_users(allowed_roles=['BusAdmin','SuperAdmin'])
def SchoolPage(request):
    school_details = SchoolDetail.objects.all()
    school_details_pk = school_details[0].id



    context = {'school_details': school_details, 'school_details_pk':school_details_pk}
    return render(request, 'bbusschool.html', context)


def SchoolEditPage(request, pk):

    school_details = SchoolDetail.objects.get(id=pk)
    form = SchoolDetailForm(instance=school_details)
    if request.method == 'POST':
        form = SchoolDetailForm(request.POST, instance=school_details)
        if form.is_valid():
            form.save()

        return redirect('bschool')

    return render(request, 'bschoolregister.html', {'form': form})



def SchoolRegisterPage(request):
    form = SchoolDetailForm()
    if request.method == 'POST':
        form = SchoolDetailForm(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect('bschool')
    return render(request, 'bschoolregister.html', {'form': form})



def BusRoutePage(request):
    train_route_details = ksrtc.BusRoute.objects.all()
    train_route_details_pk = train_route_details[0].id



    context = {'train_route_details': train_route_details, 'train_route_details_pk':train_route_details_pk}
    return render(request, 'busroute.html', context)


# def TrainSubTimes(request):
#     train_sub_time = irctc.TrainSubTime.objects.all()
#     train_sub_time_pk = train_sub_time[0].id



#     context = {'train_sub_time': train_sub_time, 'train_sub_time_pk':train_sub_time_pk}
#     return render(request, 'traintime.html', context)


def BusRouteRegister(request):
    form = BusRouteForm()
    if request.method == 'POST':
        form = BusRouteForm(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect('busroute')
    return render(request, 'busrouteregister.html', {'form': form})

def DeletebusRoute(request, pk):
    school_details = ksrtc.BusRoute.objects.get(id=pk)
    school_details.delete()
    return redirect('busroute')

def BusRouteEditPage(request, pk):

    train_place_details = ksrtc.BusRoute.objects.get(id=pk)
    form = BusRouteForm(instance=train_place_details)
    if request.method == 'POST':
        form = BusRouteForm(request.POST, instance=train_place_details)
        if form.is_valid():
            form.save()

        return redirect('busroute')

    return render(request, 'busrouteregister.html', {'form': form})

def BusesPage(request):
    train_route_details = ksrtc.Buses.objects.all()
    train_route_details_pk = train_route_details[0].id



    context = {'train_route_details': train_route_details, 'train_route_details_pk':train_route_details_pk}
    return render(request, 'busesview.html', context)

def BusesRegister(request):
    form = BusesForm()
    if request.method == 'POST':
        form = BusesForm(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect('busesview')
    return render(request, 'busesregister.html', {'form': form})

def Deletebuses(request, pk):
    school_details = ksrtc.Buses.objects.get(id=pk)
    school_details.delete()
    return redirect('busesview')

def BusesEditPage(request, pk):

    train_place_details = ksrtc.Buses.objects.get(id=pk)
    form = BusesForm(instance=train_place_details)
    if request.method == 'POST':
        form = BusesForm(request.POST, instance=train_place_details)
        if form.is_valid():
            form.save()

        return redirect('busesview')

    return render(request, 'busesregister.html', {'form': form})