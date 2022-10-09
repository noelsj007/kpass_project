from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserAdminCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def homePage(request):
    return render(request, 'home.html')

def testPage(request):
    return render(request, 'test.html')


def loginPage(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        
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



def registerPage(request):
    form = UserAdminCreationForm()
    if request.method == 'POST':
        form = UserAdminCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('first_name')
            messages.success(request, 'Account Created for ' + user + ' Please login')
            return redirect('login')
    return render(request, 'register.html', {'form': form})