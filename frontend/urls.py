from django.urls import path
from .views import *

urlpatterns = [
    path('teacher/dashboard',teacher_view, name='Teacher Dashboard'),
    path('pupil/dashboard',pupil_view, name='Pupil Dashboard'),  
    path('',account_type_select, name='Choose Account Type' ), 
]
