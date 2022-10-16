from random import choices
from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
from django.utils.translation import gettext_lazy as _

from adminapp import models as admindb
from irctc import models as traindb
from ksrtc import models as busdb

class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, email, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    
    username = None
    email = models.EmailField(_('email address'), unique=True)
    mobile = models.CharField(max_length=15, null=True, blank= True)
    is_student = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    forget_password = models.CharField(max_length=255, blank= True, null=True)
    school_name = models.ForeignKey(admindb.SchoolDetail, null=True, on_delete=models.CASCADE, related_name="student_school")

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['mobile']

    objects = CustomUserManager()

    def __str__(self):
        return self.first_name


# class CustomUser(AbstractUser):
#     username = None
#     email = models.EmailField(_('email address'), unique=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     objects = CustomUserManager()

class BusVirtualPass(models.Model):
    name = models.CharField(max_length=100, null=True)
    date = models.DateTimeField(blank=True, null=True)
    start_place = models.ForeignKey(busdb.Place, null=True, blank=True, on_delete =models.CASCADE, related_name="star_place_pass")
    end_place = models.ForeignKey(busdb.Place, null=True, blank = True, on_delete = models.CASCADE, related_name = 'end_place_pass')
    log_check = models.BooleanField(default=False, null=True)


class TrainVirtualPass(models.Model):
    name = models.CharField(max_length=100, null=True)
    date = models.DateTimeField(blank=True, null=True)
    start_place = models.ForeignKey(traindb.Place, null=True, blank=True, on_delete =models.CASCADE, related_name="star_place_pass")
    end_place = models.ForeignKey(traindb.Place, null=True, blank = True, on_delete = models.CASCADE, related_name = 'end_place_pass')
    log_check = models.BooleanField(default=False, null=True)