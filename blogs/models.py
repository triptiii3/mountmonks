from django.db import models


# Create your models here.
class blog(models.Model):
    blog_image=models.ImageField(upload_to='images/', null=True, blank=True)
    blog_title=models.CharField(max_length=100)
    blog_provider=models.CharField(max_length=500)
    destination_name=models.CharField(max_length=100)
    blog_content=models.CharField(max_length=1000)
    blog_date=models.CharField(max_length=100)
    comments=models.CharField(max_length=100)