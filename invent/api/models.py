from django.db import models
#DATABASE
# Create your models here.
#from __future__ import  unicode_literals
#from django.db import models

"""creating class"""
class Items(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
class Books(models.Model):
    name1 = models.CharField(max_length= 1000)
    price = models.IntegerField(default=100)