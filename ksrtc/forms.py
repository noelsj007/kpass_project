from .models import *
from django.forms import ModelForm


class PlaceForms(ModelForm):
    model = Place()
    fields = ['place_name', 'place_district', 'place_state']


class BusRouteForm(ModelForm):
    model = BusRoute()
    fields = ['Route_name', 'start_place', 'end_place', 'route_places']

class KsrtcSubTimeForm(ModelForm):
    model = SubTime()
    fields = ['sub_time']

class PassFormField(ModelForm):
    model = PassForm()
    fields = ['name', 'time_periode', 'school_name', 'start_place','end_place', 'age', 'address', 'adhaar_no', 'mobile','idimage','adhaarimage', 'profileimage']

