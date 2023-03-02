from .models import *
from django.forms import ModelForm

class IrctcPlaceForms(ModelForm):
    model = TrainPlace()
    fields = ['place_name', 'place_district', 'place_state']

class TrainRouteForm(ModelForm):
    model = TrainRoute()
    fields = ['Route_name', 'start_place', 'end_place', 'route_places']

class IrctcSubTimeForm(ModelForm):
    model = TrainSubTime()
    fields = ['sub_time']

class IrctcStudentPassFormField(ModelForm):
    model = TrainStudentPassForm()
    fields = ['name', 'time_periode', 'school_name', 'start_place','end_place', 'age', 'address', 'adhaar_no', 'mobile','idimage','adhaarimage', 'profileimage']

class IrctcPassFormField(ModelForm):
   class Meta:
        model = TrainPassForm
        fields = '__all__'