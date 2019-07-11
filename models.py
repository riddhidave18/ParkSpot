from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator


# Create your models here.
class users(models.Model):
	uid = models.primary_key=True
	firstname = models.CharField(max_length=40)
	lastname = models.CharField(max_length=40, null = True)
	email = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	address = models.CharField(max_length=50, null = True)
class nearbyspots(models.Model):
	sid = models.primary_key=True
	sname = models.CharField(max_length=40)
	latitude = models.DecimalField( max_digits=16, decimal_places=8)
	longitude = models.DecimalField( max_digits=16, decimal_places=8)
	area = models.CharField(max_length=40)
	city = models.CharField(max_length=40)
	type_of_parking = models.CharField(max_length=10)
	charges = models.PositiveIntegerField(validators=[MaxValueValidator(10)]) 


