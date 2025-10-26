from django.shortcuts import render

# Define the teacher dashboard
def teacher_view(request):
    return render(request, 'frontend/teacher.html')  

def pupil_view(request):
    return render(request, "frontend/pupil-dashboard.html")

def account_type_select(request):
    # TODO