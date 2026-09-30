from django import forms 
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta: 
        model = Student
        fields=['name', 'email', 'age', 'image']



class JobsForm(forms.ModelForm):
    class Meta: 
        model : Student
        fields=['_all_']