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
        form=StudentForm(request.POST, request.FILES)

        # name= request.POST.get('name')
        # email=request.POST.get('email')
        # age=request.POST.get('email')
    
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

     return render(request, 'student-details.html',{
          'student':student
     })


def edit_student(request, id):
     student = Student.objects.get(id=id)

     if request.method == "POST":
        form= StudentForm(request.POST, request.FILES,
         instance=student)

        if form.is_valid():
        
          if request.POST.get('remove_image'):
             student.image.delete(save=False)
             student.image=None

             form.save()
             return redirect('home')

        
          form.save()
          return redirect('home')
     else:
          form =StudentForm(instance=student)
  

     return render(request, 'edit-student.html',{
               'form':form
          })

def delete_student(request, id):
        student=Student.objects.get(id=id)

        if request.method == "POST":
            student.delete()
            return redirect('home')
     
        return redirect('home')





  
          

     
        