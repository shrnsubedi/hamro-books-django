from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
# Create your models here.
class CustomUser(AbstractUser):
  #validate the fields so that mobile numbers are in format
  
  phone=models.PositiveIntegerField(null=True,blank=True)
  mobile_no=models.PositiveIntegerField(null=True,blank=False)
  address_1=models.CharField(max_length=50)
  address_2=models.CharField(max_length=50)
  address_3=models.CharField(max_length=50)

  def get_absolute_url(self):
      return reverse("login")
  


