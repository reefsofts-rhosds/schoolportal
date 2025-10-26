from django.urls import path
from .views import (
    teacher_view,
    pupil_view,
)

urlpatterns = [
    path('teacher/',teacher_view, name='Teacher Dashboard'),
    path('pupil/',pupil_view, name='Pupil Dashboard'),  # View to get specific homework details
]
