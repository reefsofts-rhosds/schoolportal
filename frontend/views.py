from django.shortcuts import render

def teacher_view(request):
    return render(request, 'frontend/teacher.html')  # If in frontend/templates/

def pupil_view(request):
    return render(request, "frontend/pupil-dashboard.html")