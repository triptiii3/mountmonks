from distutils.command.upload import upload
from pyexpat import model
from django.db import models

# Create your models here.
class destinations(models.Model):
    destination_title=models.CharField(max_length=100)
    destination_image=models.ImageField(upload_to='images/', null=True, blank=True)
    
    inner_video=models.CharField(max_length=500)
    inner_details=models.CharField(max_length=100)
    inner_title=models.CharField(max_length=50)
    destination_price=models.CharField(max_length=50)
    
    def __str__(self) :
        return 'destination' + '-' + self.destination_title
class Manali(models.Model):
    old_price=models.CharField(max_length=50)
    new_price=models.CharField(max_length=50)
    main_image=models.ImageField(upload_to='images/', null=True, blank=True)
    destination_image1=models.ImageField(upload_to='images/', null=True, blank=True)
    destination_image2=models.ImageField(upload_to='images/', null=True, blank=True)
    destination_image3=models.ImageField(upload_to='images/', null=True, blank=True)
    destination_image4=models.ImageField(upload_to='images/', null=True, blank=True)
    destination_image5=models.ImageField(upload_to='images/', null=True, blank=True)
    destination_image6=models.ImageField(upload_to='images/', null=True, blank=True)
    destination=models.CharField(max_length=50,null=True, blank=True)
    time=models.CharField(max_length=50, null=True, blank=True)
    group=models.CharField(max_length=50 , null=True, blank=True)
    hiketype=models.CharField(max_length=50 , null=True, blank=True)
    difficulty=models.CharField(max_length=50, null=True, blank=True)
    pickup=models.CharField(max_length=50, null=True, blank=True)
    minage=models.CharField(max_length=50, null=True, blank=True)
    dayno1=models.CharField(max_length=50 , null=True, blank=True)
    itineraryhead1=models.CharField(max_length=50 , null=True, blank=True)
    daycontent1=models.CharField(max_length=200, null=True, blank=True )
    dayno2=models.CharField(max_length=50 , null=True, blank=True)
    itineraryhead2=models.CharField(max_length=50 , null=True, blank=True)
    daycontent2=models.CharField(max_length=200, null=True, blank=True )
    dayno3=models.CharField(max_length=50 , null=True, blank=True)
    itineraryhead3=models.CharField(max_length=50 , null=True, blank=True)
    daycontent3=models.CharField(max_length=200 , null=True, blank=True)
    dayno4=models.CharField(max_length=50, null=True, blank=True )
    itineraryhead4=models.CharField(max_length=50 , null=True, blank=True)
    daycontent4=models.CharField(max_length=200, null=True, blank=True )
    dayno5=models.CharField(max_length=50 , null=True, blank=True)
    itineraryhead5=models.CharField(max_length=50 , null=True, blank=True)
    daycontent5=models.CharField(max_length=200 , null=True, blank=True)
    dayno6=models.CharField(max_length=50 , null=True, blank=True)
    itineraryhead6=models.CharField(max_length=50 , null=True, blank=True)
    daycontent6=models.CharField(max_length=200 , null=True, blank=True)
    dayno7=models.CharField(max_length=50 , null=True, blank=True)
    itineraryhead7=models.CharField(max_length=50 , null=True, blank=True)
    daycontent7=models.CharField(max_length=200 , null=True, blank=True)
    dayno8=models.CharField(max_length=50 , null=True, blank=True)
    itineraryhead8=models.CharField(max_length=50 , null=True, blank=True)
    daycontent8=models.CharField(max_length=200 , null=True, blank=True)
    dayno9=models.CharField(max_length=50 , null=True, blank=True)
    itineraryhead9=models.CharField(max_length=50 , null=True, blank=True)
    daycontent9=models.CharField(max_length=200 , null=True, blank=True)
    dayno10=models.CharField(max_length=50 , null=True, blank=True)
    itineraryhead10=models.CharField(max_length=50 , null=True, blank=True)
    daycontent10=models.CharField(max_length=200 , null=True, blank=True)

    meetingpoint=models.CharField(max_length=50 , null=True, blank=True)
    inclusions1=models.CharField(max_length=50 , null=True, blank=True)
    inclusions2=models.CharField(max_length=50 , null=True, blank=True)
    inclusions3=models.CharField(max_length=50 , null=True, blank=True)
    inclusions4=models.CharField(max_length=50 , null=True, blank=True)
    inclusions5=models.CharField(max_length=50 , null=True, blank=True)
    exclusions1=models.CharField(max_length=50 , null=True, blank=True)
    exclusions2=models.CharField(max_length=50 , null=True, blank=True)
    exclusions3=models.CharField(max_length=50 , null=True, blank=True)
    exclusions4=models.CharField(max_length=50 , null=True, blank=True)
    exclusions5=models.CharField(max_length=50 , null=True, blank=True)
    expect1=models.CharField(max_length=400 , null=True, blank=True)
    expect2=models.CharField(max_length=400 , null=True, blank=True)
    

    
    