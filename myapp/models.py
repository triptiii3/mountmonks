import email
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class saveEnquiry(models.Model):
      name=models.CharField(max_length=50)
      email=models.CharField(max_length=50)
      dates=models.CharField(max_length=50)
      number=models.CharField(max_length=20, null=True , blank=True)



