from django.urls import path
from .views import (
    homework_detail,
    create_homework,
    get_groups_with_users,
    get_homework_ids
)

urlpatterns = [
    path('homework/<int:homework_id>/<str:detail_type>/', homework_detail, name='homework_detail'),  # View to get specific homework details
    path('homework/create/', create_homework, name='create_homework'),  # View to create homework
    path('groups/', get_groups_with_users, name='get_groups_with_users'),  # View to get all groups and their users
    path('homework/ids/', get_homework_ids, name='get_homework_ids'),  # View to get all homework IDs
]
