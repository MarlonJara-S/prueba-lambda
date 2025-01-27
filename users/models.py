from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

class User(AbstractUser):
    ROLES = (('admin', 'Admin'), ('user', 'User'))
    GENDER_CHOICES = (('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro'))

    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    role = models.CharField(max_length=5, choices=ROLES, default='user')
    is_active = models.BooleanField(default=True)

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
