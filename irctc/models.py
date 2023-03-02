from django.db import models
from adminapp import models as admindb
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

    name= models.CharField(max_length=100, default=None)
    time_periode = models.ForeignKey(TrainSubTime, on_delete = models.CASCADE, default=True)
    school_name = models.ForeignKey(admindb.SchoolDetail, on_delete = models.CASCADE, default=True)
    start_place = models.ForeignKey(TrainPlace, null=True, blank=True, on_delete =models.CASCADE, related_name="pass_start_sp")
    end_place = models.ForeignKey(TrainPlace, null=True, blank = True, on_delete = models.CASCADE, related_name = 'pass_end_sp')
    age = models.IntegerField(blank=True, null=True, default=True)
    address = models.TextField(max_length=100, blank=True, null=True)
    adhaar_no = models.CharField(max_length=200, null=True, blank=True)
    mobile = models.CharField(max_length=200, blank=True, default=None)
    adhaar_image = models.ImageField(upload_to='users/static/irctcimage/adhaar', null=True, default=None)
    profileimage = models.ImageField(upload_to='users/static/irctcimage/profileimage', null=True, default=None)
    idimage = models.ImageField(upload_to='users/static/irctcimage/idimage', null=True, default=None)

class TrainPassForm(models.Model):
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

