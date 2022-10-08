from django.db import models

# Create your models here.

class User(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Other')
    )
    name = models.CharField(max_length=50, null=True)
    username = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50, null=True)
    password = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=50, null=True, choices=GENDER)

    def __str__(self):
        return self.name

        