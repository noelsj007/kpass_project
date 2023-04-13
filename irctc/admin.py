from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(TrainRoute)
admin.site.register(TrainPlace)
admin.site.register(TrainStudentPassForm)
admin.site.register(TrainPassForm)
admin.site.register(TrainSubTime)
admin.site.register(Trains)

