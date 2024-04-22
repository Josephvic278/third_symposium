from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from users.managers import UserManager

class User(AbstractUser):
    email = models.EmailField(unique=True, null=True, db_index=True)
    username = models.CharField(max_length=50, unique=True, db_index=True)
    date_joined = models.DateTimeField(default=timezone.now)

    REQUIRED_FIELDS =  ['email']
    USERNAME_FIELD = 'username'

    objects = UserManager()

class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)