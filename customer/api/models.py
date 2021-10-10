from django.db import models
from django.contrib.auth.models import AbstractUser
from.manager import UserManager

# Create your models here.
class User(AbstractUser):
    username=None
    
    email=models.EmailField(max_length=100,unique=True)
    mobile_no=models.IntegerField(unique=True,default=True)
    objects=UserManager()
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]


class Customer(models.Model):
    profile_no=models.IntegerField(unique=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)   