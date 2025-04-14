from django.urls import path
from .views import index, create_task, update_task, delete_task, filter_tasks

urlpatterns = [
    path('', index, name='index'),  # Home route to display tasks
    path('tasks/create/', create_task, name='create_task'),  # Create new task
    path('tasks/<int:id>/update/', update_task, name='update_task'),  # Update an existing task
    path('tasks/<int:id>/delete/', delete_task, name='delete_task'),  # Delete a task
    path('tasks/filter/', filter_tasks, name='filter_tasks'),  # Filter tasks
]