from django.shortcuts import render
from .traindecorator import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from . import models as irctc
from adminapp.models import *
from adminapp.forms import *
from users.models import *
from django.db.models import Sum
# Create your views here.

@login_required(login_url='login')
@allowed_users(allowed_roles=['TrainAdmin', 'SuperAdmin'])
def homePage(request):
    # total_bus_value = PassForm.objects.aggregate(total=Sum('amount'))['total']
    total_train_value = TrainStudentPassForm.objects.aggregate(total=Sum('amount'))['total']
    total_payment =(total_train_value or 0)
    unpaid_train_pass_form = TrainStudentPassForm.objects.filter(paid=False).count()
    # unpaid_pass_form_count = PassForm.objects.filter(paid=False).count()
    total_pending_pass =unpaid_train_pass_form
    pass_form_count1 = TrainStudentPassForm.objects.filter(paid=True).count()
    pass_form_count2 = TrainPassForm.objects.filter(paid=True).count()
    pass_forms=TrainStudentPassForm.objects.filter(paid=True).order_by('-id')[:4]
    train_pass_count = (pass_form_count1 or 0) + (pass_form_count2 or 0)
    total_routes = TrainRoute.objects.all().count()
    train_route = TrainRoute.objects.all()
    print(train_pass_count)

    context={
        'total_payment' : total_payment,
        'total_pending_pass' : total_pending_pass,
        'pass_forms' : pass_forms,
        'train_pass_count' : train_pass_count,
        'total_routes' : total_routes,
        'train_route' : train_route,
        }
    return render(request, 'trainhome.html', context)

@allowed_users(allowed_roles=['TrainAdmin','SuperAdmin'])
def SchoolPage(request):
    school_details = SchoolDetail.objects.all()
    school_details_pk = school_details[0].id



    context = {'school_details': school_details, 'school_details_pk':school_details_pk}
    return render(request, 'tbusschool.html', context)


def SchoolEditPage(request, pk):

    school_details = SchoolDetail.objects.get(id=pk)
    form = SchoolDetailForm(instance=school_details)
    if request.method == 'POST':
        form = SchoolDetailForm(request.POST, instance=school_details)
        if form.is_valid():
            form.save()

        return redirect('trainadmin')

    return render(request, 'tschoolregister.html', {'form': form})



def SchoolRegisterPage(request):
    form = SchoolDetailForm()
    if request.method == 'POST':
        form = SchoolDetailForm(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect('tschool')
    return render(request, 'tschoolregister.html', {'form': form})


#Train

def TrainPlaceRegister(request):
    form = IrctcPlaceForms()
    if request.method == 'POST':
        form = IrctcPlaceForms(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect('ttrainplace')
    return render(request, 'ttrainplaceregister.html', {'form': form})


def TrainPlaceEditPage(request, pk):

    train_place_details = irctc.TrainPlace.objects.get(id=pk)
    form = IrctcPlaceForms(instance=train_place_details)
    if request.method == 'POST':
        form = IrctcPlaceForms(request.POST, instance=train_place_details)
        if form.is_valid():
            form.save()

        return redirect('ttrainplace')

    return render(request, 'ttrainplaceregister.html', {'form': form})


@allowed_users(allowed_roles=['TrainAdmin','SuperAdmin'])
def TrainPlacePage(request):
    train_place_details = irctc.TrainPlace.objects.all()
    train_place_details_pk = train_place_details[0].id



    context = {'train_place_details': train_place_details, 'train_place_details_pk':train_place_details_pk}
    return render(request, 'ttrainplace.html', context)

def DeleteTrainPlace(request, pk):
    school_details = irctc.TrainPlace.objects.get(id=pk)
    school_details.delete()
    return redirect('ttrainplace')

@allowed_users(allowed_roles=['SuperAdmin'])
def TrainAdminPage(request):
    train_user = Users.CustomUser.objects.filter(groups__name__in=['TrainAdmin'])



    context = {'train_user': train_user}
    return render(request, 'trainsystemuser.html', context)

@allowed_users(allowed_roles=['SuperAdmin'])
def TrainRoutePage(request):
    train_route_details = irctc.TrainRoute.objects.all()
    train_route_details_pk = train_route_details[0].id



    context = {'train_route_details': train_route_details, 'train_route_details_pk':train_route_details_pk}
    return render(request, 'ttrainroute.html', context)


def TrainSubTimes(request):
    train_sub_time = irctc.TrainSubTime.objects.all()
    train_sub_time_pk = train_sub_time[0].id



    context = {'train_sub_time': train_sub_time, 'train_sub_time_pk':train_sub_time_pk}
    return render(request, 'ttraintime.html', context)


def TrainRouteRegister(request):
    form = TrainRouteForm()
    if request.method == 'POST':
        form = TrainRouteForm(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect('ttrainplace')
    return render(request, 'ttrainrouteregister.html', {'form': form})

def TrainTimeRegister(request):
    form = IrctcSubTimeForm()
    if request.method == 'POST':
        form = IrctcSubTimeForm(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect('ttraintime')
    return render(request, 'ttraintimeregister.html', {'form': form})

def TrainTimeEditPage(request, pk):

    train_time_details = irctc.TrainSubTime.objects.get(id=pk)
    form = IrctcSubTimeForm(instance=train_time_details)
    if request.method == 'POST':
        form = IrctcSubTimeForm(request.POST, instance=train_time_details)
        if form.is_valid():
            form.save()

        return redirect('ttraintime')

    return render(request, 'traintimeregister.html', {'form': form})

def TrainRouteEditPage(request, pk):

    train_place_details = irctc.TrainRoute.objects.get(id=pk)
    form = TrainRouteForm(instance=train_place_details)
    if request.method == 'POST':
        form = TrainRouteForm(request.POST, instance=train_place_details)
        if form.is_valid():
            form.save()

        return redirect('ttrainroute')

    return render(request, 'trainrouteregister.html', {'form': form})


def DeleteTrainRoute(request, pk):
    school_details = irctc.TrainRoute.objects.get(id=pk)
    school_details.delete()
    return redirect('ttrainroute')

def DeleteTrainTime(request, pk):
    school_details = irctc.TrainRoute.objects.get(id=pk)
    school_details.delete()
    return redirect('ttraintime')



# Train pass forms
def TSPassPage(request):
    tspass_details = irctc.TrainStudentPassForm.objects.all()



    context = {'tspass_details': tspass_details}
    return render(request, 'ttspass.html', context)


def TSPassEditPage(request, pk):

    school_details = irctc.TrainStudentPassForm.objects.get(id=pk)
    form = IrctcStudentPassFormField(instance=school_details)
    if request.method == 'POST':
        form = IrctcStudentPassFormField(request.POST, instance=school_details)
        if form.is_valid():
            form.save()

        return redirect('ttspass')

    return render(request, 'ttspassregister.html', {'form': form})

def DeleteTSPass(request, pk):
    tspass_details = irctc.TrainStudentPassForm.objects.get(id=pk)
    tspass_details.delete()
    return redirect('ttspass')

def TPassPage(request):
    tpass_details = irctc.TrainPassForm.objects.all()



    context = {'tpass_details': tpass_details}
    return render(request, 'ttpass.html', context)


def TPassEditPage(request, pk):

    school_details = irctc.TrainPassForm.objects.get(id=pk)
    form = IrctcPassFormField(instance=school_details)
    if request.method == 'POST':
        form = IrctcPassFormField(request.POST, instance=school_details)
        if form.is_valid():
            form.save()

        return redirect('ttpass')

    return render(request, 'tpassregister.html', {'form': form})

def DeleteTPass(request, pk):
    tpass_details = irctc.TrainPassForm.objects.get(id=pk)
    tpass_details.delete()
    return redirect('ttpass')

def DeleteSchool(request, pk):
    school_details = SchoolDetail.objects.get(id=pk)
    school_details.delete()
    return redirect('tschool')



    