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

class IrctcStudentPassFormField(ModelForm):
    class Meta:
        model = TrainStudentPassForm
        fields = '__all__'
    
class IrctcPassFormField(ModelForm):
    adhaar_image =  forms.FileField(widget=forms.ClearableFileInput)
    profileimage =  forms.FileField(widget=forms.ClearableFileInput)
    class Meta:
        model = TrainPassForm
        fields = '__all__'
    
#bus pass forms

class KsrtcPassFormField(forms.ModelForm):
    # dob = forms.DateTimeField(label="Date", required=True, widget=NumberInput(attrs={'type':'date'}))
    # name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}))
    # age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}))
    # adhaar_no = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Adhaar Number'}))
    # mobile = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Mobile'}))
        

    class Meta:
        model = PassForm
        fields = '__all__'