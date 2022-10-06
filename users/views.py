from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def homePage(request):
    return render(request, 'home.html')

def testPage(request):
    return render(request, 'test.html')


def loginPage(request):
    return render(request, 'login.html')

def registerPage(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'register.html', context)
