from django.db import models

# Create your models here.

class BusRoute(models.Model):

    states = models.CharField(max_length=100, blank=True, null=True)
    districts = models.CharField(max_length=255, blank= True, null=True)
    from_place = models.CharField(max_length=100, blank= True, null=True)
    to_place = models.CharField(max_length=100, blank= True, null=True)


    def __str__(self):
        return self.from_place

class SchoolDetail(models.Model):
    school_name = models.CharField(max_length=100, blank= True, null=True)
    school_email = models.CharField(max_length=100, blank= True, null=True)
    school_address = models.CharField(max_length=100, blank= True, null=True)
    school_phone = models.CharField(max_length=15, blank= True, null=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.school_name

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