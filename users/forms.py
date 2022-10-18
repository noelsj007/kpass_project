from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from django.forms import ModelForm
from .models import *
from irctc.models import *
from ksrtc.models import *


class UserAdminCreationForm(UserCreationForm):
    """
    A Custom form for creating new users.
    """

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'mobile', 'email', 'password1', 'password2', 'is_student', 'school_name']


#train pass forms

class IrctcStudentPassFormField(ModelForm):
    model = TrainStudentPassForm()
    fields = ['tname', 'ttime_periode', 'tschool_name', 'tstart_place','tend_place', 'tage', 'taddress', 'tadhaar_no', 'tmobile','tidimage','tadhaarimage', 'tprofileimage']

class IrctcPassFormField(ModelForm):
    model = TrainPassForm()
    fields = ['tname', 'ttime_periode', 'tschool_name', 'tstart_place','tend_place', 'tage', 'taddress', 'tadhaar_no', 'tmobile','tadhaarimage', 'tprofileimage']

#bus pass forms

class KsrtcPassFormField(ModelForm):
    model = PassForm()
    fields = ['bus_name', 'bus_time_periode', 'bus_school_name', 'bus_start_place','bus_end_place', 'bus_age', 'bus_address', 'bus_adhaar_no', 'bus_mobile','bus_idimage','bus_adhaarimage', 'bus_profileimage']
