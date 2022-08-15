from ast import mod
from unicodedata import name
from django.db import models

# Create your models here.
class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    message=models.TextField()

    def __str__(self) :
        return 'message from ' + self.name + '-' + self.email

class bikingtours(models.Model):
    destination_image=models.ImageField(upload_to='images/', null=True, blank=True)
    destination_title=models.CharField(max_length=100)
    inner_video=models.CharField(max_length=500)
    inner_details=models.CharField(max_length=100)
    inner_title=models.CharField(max_length=50)
    destination_price=models.CharField(max_length=50)

class roadtours(models.Model):
    destination_image=models.ImageField(upload_to='images/', null=True, blank=True)
    destination_title=models.CharField(max_length=100)
    inner_video=models.CharField(max_length=500)
    inner_details=models.CharField(max_length=100)
    inner_title=models.CharField(max_length=50)
    destination_price=models.CharField(max_length=50)

class trekking(models.Model):
    destination_image=models.ImageField(upload_to='images/', null=True, blank=True)
    destination_title=models.CharField(max_length=100)
    inner_video=models.CharField(max_length=500)
    inner_details=models.CharField(max_length=100)
    inner_title=models.CharField(max_length=50)
    destination_price=models.CharField(max_length=50)

class spititrip(models.Model):
    destination_image=models.ImageField(upload_to='images/', null=True, blank=True)
    destination_title=models.CharField(max_length=100)
    inner_video=models.CharField(max_length=500)
    inner_details=models.CharField(max_length=100)
    inner_title=models.CharField(max_length=50)
    destination_price=models.CharField(max_length=50)

class lehtrip(models.Model):
    destination_image=models.ImageField(upload_to='images/', null=True, blank=True)
    destination_title=models.CharField(max_length=100)
    inner_video=models.CharField(max_length=500)
    inner_details=models.CharField(max_length=100)
    inner_title=models.CharField(max_length=50)
    destination_price=models.CharField(max_length=50)

class backpacktrip(models.Model):
    destination_image=models.ImageField(upload_to='images/', null=True, blank=True)
    destination_title=models.CharField(max_length=100)
    inner_video=models.CharField(max_length=500)
    inner_details=models.CharField(max_length=100)
    inner_title=models.CharField(max_length=50)
    destination_price=models.CharField(max_length=50)

class weekendtrip(models.Model):
    destination_image=models.ImageField(upload_to='images/', null=True, blank=True)
    destination_title=models.CharField(max_length=100)
    inner_video=models.CharField(max_length=500)
    inner_details=models.CharField(max_length=100)
    inner_title=models.CharField(max_length=50)
    destination_price=models.CharField(max_length=50)