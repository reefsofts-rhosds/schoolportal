from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.models import Group, User
from .models import Homework, Subject

def homework_detail(request, homework_id, detail_type):
    try:
        homework = Homework.objects.get(id=homework_id)
        
        if detail_type == 'title':
            return HttpResponse(homework.title)
        elif detail_type == 'description':
            return HttpResponse(homework.description)
        elif detail_type == 'dueDate':
            return HttpResponse(str(homework.dueDate))
        elif detail_type == "subject":
            return HttpResponse(str(homework.subject))
        elif detail_type == "attachedFile":
            return HttpResponse(str(homework.attachedFile))
        else:
            return HttpResponse('Invalid detail type', status=400)
    
    except Homework.DoesNotExist:
        return HttpResponse('Homework not found', status=404)

@csrf_exempt  # Remove this in production; it's for simplicity here.
def create_homework(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Parse JSON body
            username = data.get('username')  # Get the username
            password = data.get('password')  # Get the password
            subject_id = data.get('subject_id')  # Get the subject ID
            title = data.get('title')
            description = data.get('description')
            due_date = data.get('due_date')

            # Authenticate the user
            user = authenticate(username=username, password=password)
            if user is None:
                return HttpResponse("Invalid username or password", status=403)

            subject = Subject.objects.get(id=subject_id)

            homework = Homework(
                subject=subject,
                title=title,
                description=description,
                dueDate=due_date,
            )
            homework.save()

            return HttpResponse("Homework created successfully", status=201)
        
        except Subject.DoesNotExist:
            return HttpResponse("Subject not found", status=404)
        except Exception as e:
            return HttpResponse(str(e), status=400)

    return HttpResponse("Invalid request method", status=40)
# View to get all groups and the users in them
def get_groups_with_users(request):
    groups = Group.objects.all()
    group_data = {}

    for group in groups:
        users = group.user_set.all()  # Get users in the group
        usernames = [user.username for user in users]
        group_data[group.name] = usernames

    return JsonResponse(group_data)

# View to get all homework IDs
def get_homework_ids(request):
    homework_ids = Homework.objects.values_list('id', flat=True)  # Get all homework IDs
    return JsonResponse(list(homework_ids), safe=False)
