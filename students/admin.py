from django.contrib import admin
from .models import Student
from .models import CustomUser, Student

# Register your models here.

admin.site.register(Student)
