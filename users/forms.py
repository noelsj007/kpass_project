from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from .models import *
from irctc.models import *
from ksrtc.models import *
from django.forms.widgets import NumberInput
from adminapp import models as admindb
from .models import *
from ksrtc.models import *

class UserAdminCreationForm(UserCreationForm):
    """
    A Custom form for creating new users.
    """

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))

    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

    mobile = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Mobile'}))

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'mobile', 'email', 'password1', 'password2', 'is_student', 'school_name']


#train pass forms




class TrainStPassFormField(forms.ModelForm):
    dob = forms.DateTimeField(label="Date", required=True, widget=NumberInput(attrs={'type':'date'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}))
    adhaar_no = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Adhaar Number'}))
    mobile = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Mobile'}))
    address = forms.CharField(widget=forms.Textarea)
    adhaar_image =  forms.FileField(widget=forms.ClearableFileInput)
    profileimage =  forms.FileField(widget=forms.ClearableFileInput)
    idimage = forms.FileField(widget=forms.ClearableFileInput)
    # school_name = forms.ModelChoiceField(queryset=admindb.SchoolDetail.objects.all(), attrs={'class' : 'custom-select'})


        

    class Meta:

        model = TrainStudentPassForm
        fields = '__all__'
        widgets = {
            'school_name': forms.Select(attrs={'class': 'custom-select'},
                                            choices=admindb.SchoolDetail.objects.all()),
            'start_place': forms.Select(attrs={'class': 'custom-select'},
                                            choices=Place.objects.all()),
            'end_place': forms.Select(attrs={'class': 'custom-select'},
                                            choices=Place.objects.all()),
            'time_periode' : forms.Select(attrs={'class': 'custom-select'},
                                            choices=SubTime.objects.all())
        }


class TrainPassFormField(forms.ModelForm):
    dob = forms.DateTimeField(label="Date", required=True, widget=NumberInput(attrs={'type':'date'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}))
    adhaar_no = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Adhaar Number'}))
    mobile = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Mobile'}))
    address = forms.CharField(widget=forms.Textarea)
    adhaar_image =  forms.FileField(widget=forms.ClearableFileInput)
    profileimage =  forms.FileField(widget=forms.ClearableFileInput)
    # school_name = forms.ModelChoiceField(queryset=admindb.SchoolDetail.objects.all(), attrs={'class' : 'custom-select'})


        

    class Meta:

        model = TrainPassForm
        fields = '__all__'
        widgets = {
            'start_place': forms.Select(attrs={'class': 'custom-select'},
                                            choices=Place.objects.all()),
            'end_place': forms.Select(attrs={'class': 'custom-select'},
                                            choices=Place.objects.all()),
            'time_periode' : forms.Select(attrs={'class': 'custom-select'},
                                            choices=SubTime.objects.all())
        }


class KsrtcPassFormField(forms.ModelForm):
    dob = forms.DateTimeField(label="Date", required=True, widget=NumberInput(attrs={'type':'date'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}))
    adhaar_no = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Adhaar Number'}))
    mobile = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Mobile'}))
    address = forms.CharField(widget=forms.Textarea)
    adhaar_image =  forms.FileField(widget=forms.ClearableFileInput)
    profileimage =  forms.FileField(widget=forms.ClearableFileInput)
    idimage = forms.FileField(widget=forms.ClearableFileInput)
    # school_name = forms.ModelChoiceField(queryset=admindb.SchoolDetail.objects.all(), attrs={'class' : 'custom-select'})


        

    class Meta:

        model = PassForm
        fields = '__all__'
        widgets = {
            'school_name': forms.Select(attrs={'class': 'custom-select'},
                                            choices=admindb.SchoolDetail.objects.all()),
            'start_place': forms.Select(attrs={'class': 'custom-select'},
                                            choices=Place.objects.all()),
            'end_place': forms.Select(attrs={'class': 'custom-select'},
                                            choices=Place.objects.all()),
            'time_periode' : forms.Select(attrs={'class': 'custom-select'},
                                            choices=SubTime.objects.all())
        }