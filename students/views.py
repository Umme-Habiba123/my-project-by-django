from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
 

User=get_user_model()



def signup(request):
    context = {}

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_pass = request.POST.get('confirm_pass')

        if password != confirm_pass:
            context = {
                'error': 'Password and confirm password do not match'
            }
            return render(request, 'signup.html', context)

        if User.objects.filter(username=username).exists():
            context = {
                'error': 'Username already exists'
            }
            return render(request, 'signup.html', context)

        user = User(
            username=username
        )

        user.set_password(password)
        user.save()

        return redirect('login')

    return render(request, 'signup.html')

# login----
def login_view(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            return render(request, 'login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

          
@login_required(login_url='login')

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






  
          

     
        