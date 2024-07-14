from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Tweet(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.TextField(max_length=999)
    photo=models.ImageField(upload_to='photos/',blank=True,null=True)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.user.username}-{self.text[:10]}"
    

class Contactus(models.Model):
    name=models.CharField(max_length=200)
    info=models.CharField(max_length=1000)
    email=models.TextField(max_length=200)
    mobile=models.CharField(max_length=200)
    date_added=models.DateField(auto_now=True)


    def __str__(self):
        return self.name
