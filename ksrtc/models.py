from django.db import models
from adminapp import models as admindb
import datetime
from django.contrib.auth import get_user_model
from django.conf import settings
from datetime import timedelta
# Create your models here.

class Place(models.Model):
    place_name = models.CharField(max_length=100, null=True, blank=True)
    place_district = models.CharField(max_length=100, null=True, blank=True)
    place_state = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.place_name



class BusRoute(models.Model):
    Route_name = models.CharField(max_length=100, null=True, blank = True)
    start_place = models.ForeignKey(Place, null=True, blank=True, on_delete =models.CASCADE, related_name="start")
    end_place = models.ForeignKey(Place, null=True, blank = True, on_delete = models.CASCADE, related_name = 'end')
    route_places = models.ManyToManyField(Place, related_name = 'betweenplace')


    def __str__(self):
        return self.Route_name

class Buses(models.Model):
    Route_name = models.ForeignKey(BusRoute, on_delete=models.CASCADE, related_name='buses_route')
    bus_number = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.bus_number


class SubTime(models.Model):
    sub_time = models.IntegerField(null=True)
    sub_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.sub_name


class PassForm(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default=None)
    time_periode = models.ForeignKey(SubTime, on_delete=models.CASCADE, default=True)
    school_name = models.ForeignKey(admindb.SchoolDetail, on_delete=models.CASCADE, default=True)
    start_place = models.ForeignKey(Place, null=True, blank=True, on_delete=models.CASCADE, related_name="pass_start")
    end_place = models.ForeignKey(Place, null=True, blank=True, on_delete=models.CASCADE, related_name='pass_end')
    age = models.IntegerField(blank=True, null=True, default=True)
    dob = models.DateField(default=datetime.date.today)
    address = models.CharField(max_length=100, blank=True, null=True)
    adhaar_no = models.CharField(max_length=200, null=True, blank=True)
    mobile = models.CharField(max_length=200, blank=True, default=None)
    idimage = models.ImageField(upload_to='ksrtcimage/idimage', null=True, default=None)
    adhaar_image = models.ImageField(upload_to='ksrtcimage/adhaar', null=True, default=None)
    profileimage = models.ImageField(upload_to='ksrtcimage/profileimage', null=True, default=None)
    bus_rate = models.IntegerField(null=True)
    amount = models.IntegerField(null=True, blank=True)
    order_id = models.CharField(max_length=255, null=True, blank=True)
    signature = models.CharField(max_length=255, null=True, blank=True)
    payment_id = models.CharField(max_length=255, null=True, blank=True)
    paid = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    verification_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Calculate amount based on bus_rate and sub_time
        sub_time = self.time_periode.sub_time
        bus_rate = self.bus_rate or 0.0
        self.amount = int((0.1 * bus_rate * sub_time)*2)

        super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        subtime = self.time_periode.sub_time
        verification_date = self.verification_date or 0.0
        if self.verification_date:

            self.end_date = verification_date + timedelta(days=subtime)
            
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name

