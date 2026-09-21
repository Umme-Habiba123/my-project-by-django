from django.urls import path 
from .views import * 



urlpatterns = [
    path('', home, name='home'),


    path('add-student/', add_student, name='add_student'),
    
    path('student/<int:id>/', student_details, name='student_details'),

    path('edit-student/<int:id>/', edit_student, name='edit-student'),

    path('delete-student/<int:id>/',delete_student, name='delete_student'),

    path('signup/', signup, name='signup' ),

    path('login/', login_view, name='login'),

    path('logout/', logout_view, name='logout'),



    ]
