from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser) :
    display_name = models.CharField(max_length=255)
    otp = models.IntegerField(null=True, blank=True )



class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    age = models.IntegerField()

    image=models.ImageField(
    upload_to='students/', 
    null=True, 
    blank=True)

    def __str__(self):
        return self.name


class Job(models.Model):
    companyname = models.CharField(max_length=200)
    position=models.CharField(max_length=200)
    vacancy=models.IntegerField()
    education=models.CharField(max_length=100)
    skills=models.CharField(max_length=100)

    image=models.ImageField(
         upload_to='job',
         blank=True,
         null=True   ,
        )
    
    def __str__(self):
           return self.name
    