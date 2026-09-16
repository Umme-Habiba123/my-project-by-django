from django.shortcuts import render
from .models import Students


def home(request):
    Students = Students.object.all()
    return render(request, 'students/index.html',{
        'students' : Students
    })