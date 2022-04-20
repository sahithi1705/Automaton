from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime
class Bookings(models.Model):
	First_name				= models.CharField(default='null',max_length=30)
	Last_name				= models.CharField(default='null',max_length=30)
	Vehicle					= models.CharField(max_length=30)
	Address					= models.CharField(max_length=30)
	Phone					= models.CharField(max_length=30)
	Time					= models.DateTimeField(default=datetime.datetime.now())
	
