from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

def home(request):
    students = Student.objects.all()

    return render(request, 'index.html',{
        'students' : students
    })


def add_student(request):
    if request.method == 'POST':
        # name= request.POST.get('name')
        # email=request.POST.get('email')
        # age=request.POST.get('email')
        form=StudentForm(request.POST)

        # Student.objects.create(
        #     name=name,
        #     email=email,
        #     age=age,

        # )

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
            form = StudentForm()

    return render(request, 'add-student.html',{
            'form': form
        })

def student_details(request, id):
     student=Student.objects.get(id=id)

     return render(request, 'student_details.html',{
          'student':student
     })


     
        