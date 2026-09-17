from django.urls import path 
from .views import * 

urlpatterns = [
    path('', home, name='home'),


    path('add-student/', add_student, name='add_student'),
    path('student/<int:id>/', student_details, name='student_details'),

    
]