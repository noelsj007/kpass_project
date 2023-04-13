
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

    place_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Place Name'}))
    place_district = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Place District'}))
    place_state = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Place State'}))


    class Meta:
        model = Place
        fields = '__all__'


class BusRouteForm(ModelForm):
    Route_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Route  Name'}))
    start_place = forms.ModelChoiceField(queryset=Place.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    end_place = forms.ModelChoiceField(queryset=Place.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    route_places = forms.ModelMultipleChoiceField(queryset=Place.objects.all(), widget=forms.SelectMultiple(attrs={'class': 'form-control'}))

    class Meta:
        model = BusRoute
        fields = '__all__'

class KsrtcSubTimeForm(ModelForm):
    sub_time = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Number of Days of Validity'}))
    sub_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sub Name'}))


    class Meta:
        model = SubTime
        fields = '__all__'

class KsrtcPassFormField(ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    time_periode = forms.ModelChoiceField(queryset=SubTime.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    school_name = forms.ModelChoiceField(queryset=admindb.SchoolDetail.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    start_place = forms.ModelChoiceField(queryset=Place.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    end_place = forms.ModelChoiceField(queryset=Place.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}))
    dob = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date of Birth'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}))
    adhaar_no = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Aadhaar Number'}))
    mobile = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile'}))
    idimage = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    adhaar_image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    profileimage = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    bus_rate = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Bus Rate'}))
    

    class Meta:
        model = PassForm
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'time_periode': forms.Select(attrs={'class': 'form-control'}),
            'school_name': forms.Select(attrs={'class': 'form-control'}),
            'start_place': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Start Place'}),
            'end_place': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'End Place'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'adhaar_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adhaar No'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile'}),
            'idimage': forms.FileInput(attrs={'class': 'form-control-file'}),
            'adhaar_image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'profileimage': forms.FileInput(attrs={'class': 'form-control-file'}),
            'bus_rate': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Bus Rate'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Amount'}),
            'order_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Order ID'}),
            'signature': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Signature'}),
            'payment_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Payment ID'}),
            'paid': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_verified': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'verification_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

# trian forms for super admin

class IrctcPlaceForms(ModelForm):

    train_place_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Place Name'}))
    train_place_district = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Place District'}))
    train_place_state = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Place State'}))

    class Meta:
        model = TrainPlace
        fields = '__all__'

class TrainRouteForm(ModelForm):
    train_route_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Train Route Name'}))
    train_start_place = forms.ModelChoiceField(queryset=TrainPlace.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    train_end_place = forms.ModelChoiceField(queryset=TrainPlace.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    train_route_places = forms.ModelMultipleChoiceField(queryset=TrainPlace.objects.all(), widget=forms.SelectMultiple(attrs={'class': 'form-control'}))

    class Meta:
        model = TrainRoute
        fields = '__all__'

class IrctcSubTimeForm(ModelForm):
    sub_time = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Sub Time'}))
    sub_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sub Name'}))


    class Meta:
        
        model = TrainSubTime
        fields = '__all__'

class IrctcStudentPassFormField(ModelForm):
    class Meta:
        model = TrainStudentPassForm
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'time_periode': forms.Select(attrs={'class': 'form-control'}),
            'school_name': forms.Select(attrs={'class': 'form-control'}),
            'start_place': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Start Place'}),
            'end_place': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'End Place'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'adhaar_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adhaar No'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile'}),
            'idimage': forms.FileInput(attrs={'class': 'form-control-file'}),
            'adhaar_image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'profileimage': forms.FileInput(attrs={'class': 'form-control-file'}),
            'bus_rate': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Bus Rate'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Amount'}),
            'order_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Order ID'}),
            'signature': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Signature'}),
            'payment_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Payment ID'}),
            'paid': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_verified': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'verification_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class IrctcPassFormField(ModelForm):
    class Meta:
        model = TrainPassForm
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'time_periode': forms.Select(attrs={'class': 'form-control'}),
            'start_place': forms.Select(attrs={'class': 'form-control'}),
            'end_place': forms.Select(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'adhaar_no': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'adhaar_image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'profileimage': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'trainst_rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'order_id': forms.TextInput(attrs={'class': 'form-control'}),
            'signature': forms.TextInput(attrs={'class': 'form-control'}),
            'payment_id': forms.TextInput(attrs={'class': 'form-control'}),
            'paid': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'verification_date': forms.DateInput(attrs={'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control'})
        }