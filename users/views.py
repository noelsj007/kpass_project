from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserAdminCreationForm

# Create your views here.

def homePage(request):
    return render(request, 'home.html')

def testPage(request):
    return render(request, 'test.html')


def loginPage(request):
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
            return redirect('login.html')
        else:
            print('error')
    return render(request, 'register.html', {'form': form})