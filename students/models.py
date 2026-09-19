from django.db import models

# Create your models here.
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