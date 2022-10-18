import email
from random import choices
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _


# Create your models here.

class CustomAdminManager(BaseUserManager):
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

class CustomAdmin(AbstractUser):
    
    username = None
    user_permissions = None
    groups= None
    email = models.EmailField(_('email address'), unique=True)
    mobile = models.CharField(max_length=15, null=True, blank= True)
    is_verified = models.BooleanField(default=False)
    forget_password = models.CharField(max_length=255, blank= True, null=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['mobile']

    objects = CustomAdminManager()

    def __str__(self):
        return self.first_name


class SchoolDetail(models.Model):
    school_name = models.CharField(max_length=100, blank= True, null=True)
    school_place = models.CharField(max_length=100, blank= True, null=True)
    school_email = models.CharField(max_length=100, blank= True, null=True)
    school_address = models.CharField(max_length=100, blank= True, null=True)
    school_phone = models.CharField(max_length=15, blank= True, null=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.school_name