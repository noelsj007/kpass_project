from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserAdminCreationForm, KsrtcPassFormField, IrctcPassFormField
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorator import *
from .models import *
from ksrtc.models import *

# Create your views here.

# @login_required(login_url='login')
def homePage(request):
    return render(request, 'home.html')

@login_required(login_url='login')
# @allowed_users(allowed_roles=['customer', 'superadmin', 'admin'])

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



# def BusPassForm(request):
#     school = admindb.SchoolDetail.objects.all()
#     place = Place.objects.all()
#     subtime = SubTime.objects.all()
#     if request.method == 'POST':
#         name = request.POST.get("name")
#         age = request.POST.get("age")
#         dob = request.POST.get("dob")
#         mobile = request.POST.get("mobile")
#         adhaar_no = request.POST.get("adhaar_no")
#         address = request.POST.get("address")
#         school_name = request.POST.get("school_name")
#         start_place = request.POST.get("start_place")
#         end_place = request.POST.get("end_place")
#         time_periode = request.POST.get("time_periode")
#         profileimage = request.FILES.get("profileimage")
#         idimage = request.FILES.get("idimage")
#         adhaar_image = request.FILES.get("adhaar_image")
#         try:
#             buspassform = PassForm(name=name, age=age, dob=dob, mobile=mobile, adhaar_no=adhaar_no, address=address, school_name=school_name, start_place=start_place, end_place=end_place, time_periode=time_periode, profileimage=profileimage, idimage=idimage, adhaar_image=adhaar_image)
#             buspassform.save()
#             messages.success(request, 'application submitted')
#             return redirect('dash')
#         except:
#             messages.error(request, 'Error in submitting your appliction')
#             return redirect('buspassform')
#         print(form.error)

        
#     return render(request, 'buspassform.html', {'school':school, 'place':place, 'subtime':subtime})

from django.contrib.auth.decorators import login_required

@login_required
def BusPassForm(request):
    user = request.user
    if request.method == 'POST':
        form = KsrtcPassFormField(request.POST, request.FILES)
        if form.is_valid():
            # Get the start and end places from the form data
            
            start_place = form.cleaned_data['start_place']
            end_place = form.cleaned_data['end_place']
            start_place_g = get_geocode('start_place')
            end_place_g = get_geocode('end_place')

            # Calculate the distance between the start and end places
            distance = calculate_distance(start_place, end_place)

            # Calculate the fare for the distance
            fare = calculate_fare(distance)

            # Set the user field of the PassForm instance to the current user
            pass_form = form.save(commit=False)
            pass_form.user = request.user
            print(fare,distance)
            pass_form.save()

            messages.success(request, 'application submitted')
            return redirect('dash')

        else:
            messages.error(request, 'Error in submitting your application')
            print(form.errors)
            return redirect('buspassform')
    else:
        form = KsrtcPassFormField(initial={'user': user})

    return render(request, 'buspassform.html', {'form':form, 'user': user})


import requests

import requests

def get_geocode(place):
    url = "https://nominatim.openstreetmap.org/search"
    params = {"q": place, "format": "json"}
    response = requests.get(url, params=params).json()
    if response:
        latitude = response[0]["lat"]
        longitude = response[0]["lon"]
        return latitude, longitude
    else:
        return None, None


import requests
import json

import requests
import json

def calculate_distance(start_place, end_place):
    # Construct the API URL for the OpenStreetMap API
    url = f"https://router.project-osrm.org/route/v1/driving/{start_place.longitude},{start_place.latitude};{end_place.longitude},{end_place.latitude}?overview=false"

    # Make a request to the API and parse the response
    response = requests.get(url)
    data = json.loads(response.text)

    # Get the distance in meters
    distance_meters = data['routes'][0]['distance']

    # Convert the distance to kilometers
    distance_km = distance_meters / 1000

    return distance_km




def calculate_fare(distance):
    # Base fare for the first 10 km
    base_fare = 10
    
    # Fare per km beyond the first 10 km
    fare_per_km = 0.5
    
    # Calculate the fare based on the distance
    if distance <= 0:
        return 0
    elif distance <= 10:
        return base_fare
    else:
        additional_distance = distance - 10
        additional_fare = additional_distance * fare_per_km
        total_fare = base_fare + additional_fare
        return total_fare


import requests
import json

# def calculate_distance(start_place, end_place):
#     api_key = 'wcDYwipzkB01G4b57LcshuzmU5tX9NvK8G7pS73j_Ko'
#     base_url = 'https://route.ls.hereapi.com/routing/7.2/calculateroute.json'

#     start_gcode = f'{start_place.gcode_lat},{start_place.gcode_lng}'
#     end_gcode = f'{end_place.gcode_lat},{end_place.gcode_lng}'

#     payload = {
#         'apiKey': api_key,
#         'waypoint0': start_gcode,
#         'waypoint1': end_gcode,
#         'mode': 'fastest;car;traffic:enabled'
#     }

#     response = requests.get(base_url, params=payload)
#     if response.status_code == 200:
#         data = json.loads(response.content.decode('utf-8'))
#         distance = data['response']['route'][0]['summary']['distance'] / 1000.0  # convert to km
#         return distance
#     else:
#         return None


@login_required
def view_pass_forms(request):
    user = request.user
    pass_forms = PassForm.objects.filter(user=user)
    return render(request, 'viewpassforms.html', {'pass_forms': pass_forms})

def TrainPassForm(request):
    user = request.user
    if request.method == 'POST':
        form = IrctcPassFormField(request.POST, request.FILES)
        if form.is_valid():
            pass_form=form.save(commit=False)
            pass_form.user = request.user
            pass_form.save()
            messages.success(request, 'application submitted')
            return redirect('dash')

        else:
            messages.error(request, 'Error in submitting your application')
            print(form.errors)
            return redirect('trainpassform')
    else:
        form = IrctcPassFormField(initial={'user': user})
    return render(request, 'trainpassform.html', {'form':form, 'user': user})