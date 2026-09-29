from django.db import models
from django import models, include

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


