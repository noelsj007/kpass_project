
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import *
from ksrtc.models import PassForm, Place, BusRoute, SubTime
from irctc.models import *
from django import forms
from django.forms import ModelForm


class UserAdminCreationForm(UserCreationForm):
    """
    A Custom form for creating new users.
    """
    # first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))

    # last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

    # mobile = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Mobile'}))

    # email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    
    # password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    # password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'mobile', 'email', 'password1', 'password2']


class SchoolDetailForm(ModelForm):

    school_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'School Name'}))
    school_place = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'School Place'}))
    school_email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    school_phone = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Mobile'}))
    school_address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}))




    class Meta:
        model = SchoolDetail
        fields = '__all__'

# forms for ksrtc admin
class KstrcPlaceForms(ModelForm):

    class Meta:
        model = Place
        fields = '__all__'


class BusRouteForm(ModelForm):

    class Meta:
        model = BusRoute
        fields = '__all__'

class KsrtcSubTimeForm(ModelForm):

    class Meta:
        model = SubTime
        fields = '__all__'

class KsrtcPassFormField(ModelForm):

    class Meta:
        model = PassForm
        fields = '__all__'

# trian forms for super admin

class IrctcPlaceForms(ModelForm):

    class Meta:
        model = TrainPlace
        fields = '__all__'

class TrainRouteForm(ModelForm):

    class Meta:
        model = TrainRoute
        fields = '__all__'

class IrctcSubTimeForm(ModelForm):

    class Meta:
        
        model = TrainSubTime
        fields = '__all__'

class IrctcStudentPassFormField(ModelForm):
    class Meta:
        model = TrainStudentPassForm
        fields = '__all__'

class IrctcPassFormField(ModelForm):
    class Meta:
        model = TrainPassForm
        fields = '__all__'