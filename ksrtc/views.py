from django.shortcuts import render
from .busdecorators import *
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
@bus_allowed_users(allowed_roles=['BusAdmin'])
def homePage(request):
    return render(request, 'bushome.html')



