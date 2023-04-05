from django.db import models
from adminapp import models as admindb
from django.conf import settings
import datetime
from datetime import timedelta
# Create your models here.


class TrainPlace(models.Model):
    train_place_name = models.CharField(max_length=100, null=True, blank=True)
    train_place_district = models.CharField(max_length=100, null=True, blank=True)
    train_place_state = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.train_place_name



class TrainRoute(models.Model):
    train_route_name = models.CharField(max_length=100, null=True, blank = True)
    train_start_place = models.ForeignKey(TrainPlace, null=True, blank=True, on_delete =models.CASCADE, related_name="start")
    train_end_place = models.ForeignKey(TrainPlace, null=True, blank = True, on_delete = models.CASCADE, related_name = 'end')
    train_route_places = models.ManyToManyField(TrainPlace, related_name = 'betweenplace')


    def __str__(self):
        return self.train_route_name


class TrainSubTime(models.Model):
    sub_time = models.IntegerField(null=True)
    sub_name = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.sub_name



class TrainStudentPassForm(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    name= models.CharField(max_length=100, default=None)
    time_periode = models.ForeignKey(TrainSubTime, on_delete = models.CASCADE, default=True)
    school_name = models.ForeignKey(admindb.SchoolDetail, on_delete = models.CASCADE, default=True)
    start_place = models.ForeignKey(TrainPlace, null=True, blank=True, on_delete =models.CASCADE, related_name="pass_start_sp")
    end_place = models.ForeignKey(TrainPlace, null=True, blank = True, on_delete = models.CASCADE, related_name = 'pass_end_sp')
    age = models.IntegerField(blank=True, null=True, default=True)
    dob = models.DateField(default=datetime.date.today)
    address = models.TextField(max_length=100, blank=True, null=True)
    adhaar_no = models.CharField(max_length=200, null=True, blank=True)
    mobile = models.CharField(max_length=200, blank=True, default=None)
    adhaar_image = models.ImageField(upload_to='users/static/irctcimage/adhaar', null=True, default=None)
    profileimage = models.ImageField(upload_to='users/static/irctcimage/profileimage', null=True, default=None)
    idimage = models.ImageField(upload_to='users/static/irctcimage/idimage', null=True, default=None)
    train_rate = models.IntegerField(null=True)
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
        train_rate = self.bus_rate or 0.0
        self.amount = int((0.1 * train_rate * sub_time)*2)

        super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        subtime = self.time_periode.sub_time
        verification_date = self.verification_date or 0.0
        if self.verification_date:

            self.end_date = verification_date + timedelta(days=subtime)
            
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name

class TrainPassForm(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    name= models.CharField(max_length=100, default=None)
    time_periode = models.ForeignKey(TrainSubTime, on_delete = models.CASCADE, default=True)
    start_place = models.ForeignKey(TrainPlace, null=True, blank=True, on_delete =models.CASCADE, related_name="pass_start_tp")
    end_place = models.ForeignKey(TrainPlace, null=True, blank = True, on_delete = models.CASCADE, related_name = 'pass_end_tp')
    age = models.IntegerField(blank=True, null=True, default=True)
    address = models.TextField(max_length=100, blank=True, null=True)
    adhaar_no = models.CharField(max_length=200, null=True, blank=True)
    mobile = models.CharField(max_length=200, blank=True, default=None)
    adhaar_image = models.ImageField(upload_to='irctcimage/adhaar', null=True, default=None)
    profileimage = models.ImageField(upload_to='irctcimage/profileimage', null=True, default=None)
    trainst_rate = models.IntegerField(null=True)
    amount = models.IntegerField(null=True, blank=True)
    order_id = models.CharField(max_length=255, null=True, blank=True)
    signature = models.CharField(max_length=255, null=True, blank=True)
    payment_id = models.CharField(max_length=255, null=True, blank=True)
    paid = models.BooleanField(default=False)
    verification_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Calculate amount based on bus_rate and sub_time
        sub_time = self.time_periode.sub_time
        trainst_rate = self.bus_rate or 0.0
        self.amount = int((0.2 * train_rate * sub_time)*2)

        super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        subtime = self.time_periode.sub_time
        verification_date = self.verification_date or 0.0
        if self.verification_date:

            self.end_date = verification_date + timedelta(days=subtime)
            
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name

