from django.shortcuts import render
from .models import Student


def home(request):
    students = Student.objects.all()

    return render(request, 'students/index.html',{
        'students' : students
    })