from django.db import models

# Create your models here.
class blog(models.Model):
    blog_image=models.ImageField(upload_to='images/', null=True, blank=True)
    blog_title=models.CharField(max_length=100)
    blog_provider=models.CharField(max_length=500)