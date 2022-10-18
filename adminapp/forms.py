from attr import fields
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

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'mobile', 'email', 'password1', 'password2']


class SchoolDetailForm(ModelForm):
    model = SchoolDetail()
    fields = ['bus_school_name', 'bus_school_place', 'bus_school_address', 'bus_school_phone', 'bus_school_email']


# forms for ksrtc admin
class KstrcPlaceForms(ModelForm):
    model = Place()
    fields = ['bus_place_name', 'bus_place_district', 'bus_place_state']


class BusRouteForm(ModelForm):
    model = BusRoute()
    fields = ['bsu_Route_name', 'bsu_start_place', 'bus_end_place', 'bus_route_places']

class KsrtcSubTimeForm(ModelForm):
    model = SubTime()
    fields = ['bus_sub_time']

class KsrtcPassFormField(ModelForm):
    model = PassForm()
    fields = ['bus_name', 'bus_time_periode', 'bus_school_name', 'bus_start_place','bus_end_place', 'bus_age', 'bus_address', 'bus_adhaar_no', 'bus_mobile','bus_idimage','bus_adhaarimage', 'bus_profileimage']

# trian forms for super admin

class IrctcPlaceForms(ModelForm):
    model = TrainPlace()
    fields = ['tplace_name', 'tplace_district', 'tplace_state']

class TrainRouteForm(ModelForm):
    model = TrainRoute()
    fields = ['tRoute_name', 'tstart_place', 'tend_place', 'troute_places']

class IrctcSubTimeForm(ModelForm):
    model = TrainSubTime()
    fields = ['tsub_time']

class IrctcStudentPassFormField(ModelForm):
    model = TrainStudentPassForm()
    fields = ['tname', 'ttime_periode', 'tschool_name', 'tstart_place','tend_place', 'tage', 'taddress', 'tadhaar_no', 'tmobile','tidimage','tadhaarimage', 'tprofileimage']

class IrctcPassFormField(ModelForm):
    model = TrainPassForm()
    fields = ['tname', 'ttime_periode', 'tschool_name', 'tstart_place','tend_place', 'tage', 'taddress', 'tadhaar_no', 'tmobile','tadhaarimage', 'tprofileimage']
