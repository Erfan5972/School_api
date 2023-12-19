from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.hashers import make_password

from .validators import check_phone, isnumeric
# Create your models here.


class MyUserManager(UserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        return super().create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('first_name', 'admin')
        return super().create_superuser(username, email, password, **extra_fields)


class User(AbstractUser):
    national_code = models.CharField(max_length=11, unique=True, validators=[isnumeric])
    phone_number = models.CharField(max_length=11, unique=True, validators=[check_phone])
    bio = models.TextField(null=True, blank=True)
    objects = MyUserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'phone_number', 'password']

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.last_name}//{self.id}'