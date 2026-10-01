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
        
        
class RegistrationForm(UserCreationForm):
    
    username=forms.CharField(lebel='username', widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Input username',
        }
    ))
    
    email=forms.CharField(lebel='Email',widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Input Email'
            
        }
    ))
    
    password1=forms.CharField(lebel='password', widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'Inpur Password'
        }
    ))
    
    password2=forms.CharField(lebel='password', widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'palceholder':'Input Password'
        }
    ))
    
    
class LoginForm(AuthenticationForm):
    
    username=forms.CharField(lebel='Username', widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Imput Password'
        }
    ))
    
    password=forms.CharField(lebel='Password',widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Input Password'
        }
    ))
    
    class Meta:
        model=CustomsUser
        fields=['username', 'password']
    