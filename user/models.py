from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group, Permission

from .validators import check_phone, isnumeric


class MyUserManager(UserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        return super().create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('first_name', 'admin')
        return super().create_superuser(username, email, password, **extra_fields)


class User(AbstractUser):
    national_code = models.CharField(max_length=11, unique=True, db_index=True, validators=[isnumeric])
    phone_number = models.CharField(max_length=11, unique=True, db_index=True, validators=[check_phone])
    bio = models.TextField(null=True, blank=True)
    groups = models.ManyToManyField(Group, related_name='users', db_index=True, blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='users', db_index=True, blank=True)

    objects = MyUserManager()
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['password']

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.username}//{self.id}'