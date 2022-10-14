from django.db import models

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

class SchoolDetail(models.Model):
    school_name = models.CharField(max_length=100, blank= True, null=True)
    school_email = models.CharField(max_length=100, blank= True, null=True)
    school_address = models.CharField(max_length=100, blank= True, null=True)
    school_phone = models.CharField(max_length=15, blank= True, null=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.school_name

class SubTime(models.Model):
    sub_time = models.IntegerField(null=True)
    sub_price = models.IntegerField(null=True, blank=True)


class PassForm(models.Model):

    TIME=(
        ('onemonth', 'onemonth'),
        ('threemonths', 'threemonths'),
        ('sixmonths', 'sixmonths'),
        ('oneyear', 'oneyear'),
    )
    time_periode = models.CharField(max_length=50, blank= True, null=True, choices=TIME)
    age = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)

class StudentPassForm(models.Model):

    TIME=(
        ('onemonth', 'onemonth'),
        ('threemonths', 'threemonths'),
        ('sixmonths', 'sixmonths'),
        ('oneyear', 'oneyear'),
    )
    time_periode = models.CharField(max_length=50, blank= True, null=True, choices=TIME)
    age = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)