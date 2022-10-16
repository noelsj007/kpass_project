from django.db import models
from adminapp import models as admindb
# Create your models here.


class Place(models.Model):
    place_name = models.CharField(max_length=100, null=True, blank=True)
    place_district = models.CharField(max_length=100, null=True, blank=True)
    place_state = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.place_name



class TrainRoute(models.Model):
    Route_name = models.CharField(max_length=100, null=True, blank = True)
    start_place = models.ForeignKey(Place, null=True, blank=True, on_delete =models.CASCADE, related_name="start")
    end_place = models.ForeignKey(Place, null=True, blank = True, on_delete = models.CASCADE, related_name = 'end')
    route_places = models.ManyToManyField(Place, related_name = 'betweenplace')


    def __str__(self):
        return self.Route_name


class SubTime(models.Model):
    sub_time = models.IntegerField(null=True)



class StudentPassForm(models.Model):

    name= models.CharField(max_length=100, default=None)
    time_periode = models.ForeignKey(SubTime, on_delete = models.CASCADE, default=True)
    school_name = models.ForeignKey(admindb.SchoolDetail, on_delete = models.CASCADE, default=True)
    start_place = models.ForeignKey(Place, null=True, blank=True, on_delete =models.CASCADE, related_name="pass_start_sp")
    end_place = models.ForeignKey(Place, null=True, blank = True, on_delete = models.CASCADE, related_name = 'pass_end_sp')
    age = models.IntegerField(blank=True, null=True, default=True)
    address = models.TextField(max_length=100, blank=True, null=True)
    adhaar_no = models.CharField(max_length=200, null=True, blank=True)
    mobile = models.CharField(max_length=200, blank=True, default=None)
    adhaar_image = models.ImageField(upload_to='static/irctcimage/adhaar', null=True, default=None)
    profileimage = models.ImageField(upload_to='static/irctcimage/profileimage', null=True, default=None)
    idimage = models.ImageField(upload_to='static/irctcimage/idimage', null=True, default=None)

class PassForm(models.Model):
    name= models.CharField(max_length=100, default=None)
    time_periode = models.ForeignKey(SubTime, on_delete = models.CASCADE, default=True)
    start_place = models.ForeignKey(Place, null=True, blank=True, on_delete =models.CASCADE, related_name="pass_start_tp")
    end_place = models.ForeignKey(Place, null=True, blank = True, on_delete = models.CASCADE, related_name = 'pass_end_tp')
    age = models.IntegerField(blank=True, null=True, default=True)
    address = models.TextField(max_length=100, blank=True, null=True)
    adhaar_no = models.CharField(max_length=200, null=True, blank=True)
    mobile = models.CharField(max_length=200, blank=True, default=None)
    adhaar_image = models.ImageField(upload_to='static/irctcimage/adhaar', null=True, default=None)
    profileimage = models.ImageField(upload_to='static/irctcimage/profileimage', null=True, default=None)

