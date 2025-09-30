from django.db import models
from django.contrib.auth.models import AbstractUser

# user model which extends AbstractUser
class User(AbstractUser):
    pass