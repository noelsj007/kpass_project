from django.db import models

# Create your models here.

class TrainRoutes(models.Model):

    states = models.CharField(max_length=100, blank=True, null=True)
    districts = models.CharField(max_length=255, blank= True, null=True)
    from_place = models.CharField(max_length=100, blank= True, null=True)
    to_place = models.CharField(max_length=100, blank= True, null=True)

    
    def __str__(self):
        return self.states
