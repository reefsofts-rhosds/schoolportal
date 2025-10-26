from django.urls import path
from .views import *

urlpatterns = [
    path('teacher/dashboard',teacher_view, name='Teacher Dashboard'), #  Define teacher dashboard
    path('pupil/dashboard',pupil_view, name='Pupil Dashboard'),  # Define pupil dashboard
    path('',account_type_select, name='Choose Account Type' ),  # Define Account type choice
]
