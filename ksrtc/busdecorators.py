from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate

def bus_unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):

        if request.user.is_authenticated:
            return redirect('bushome')

        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def bus_allowed_users(allowed_roles = []):

    
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)

            else:
                return render(request, '404.html')

        return wrapper_func

    return decorator