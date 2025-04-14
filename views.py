# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Task

# Home route to display all tasks
def index(request):
    tasks = Task.objects.all()  # Get all tasks
    return render(request, 'index.html', {'tasks': tasks})

# Create a new task
def create_task(request):
    if request.method == 'POST':
        # Get data from the form
        entity_name = request.POST.get('entity_name')
        task_type = request.POST.get('task_type')
        task_time = request.POST.get('task_time')
        contact_person = request.POST.get('contact_person')
        note = request.POST.get('note')
        status = request.POST.get('status', 'open')  # Default status is 'open'

        # Create and save the task
        task = Task(
            entity_name=entity_name,
            task_type=task_type,
            task_time=task_time,
            contact_person=contact_person,
            note=note,
            status=status
        )
        task.save()  # Save to database

        return redirect('index')  # Redirect to the task list page

    return render(request, 'task_form.html', {'action': 'Create'})

# Update an existing task
def update_task(request, id):
    task = get_object_or_404(Task, id=id)  # Get task by id or return 404

    if request.method == 'POST':
        # Get data from the form
        task.entity_name = request.POST.get('entity_name')
        task.task_type = request.POST.get('task_type')
        task.task_time = request.POST.get('task_time')
        task.contact_person = request.POST.get('contact_person')
        task.note = request.POST.get('note')
        task.status = request.POST.get('status')

        task.save()  # Save the updated task

        return redirect('index')  # Redirect to the task list page

    # Render the form with existing task data for editing
    return render(request, 'task_form.html', {'action': 'Update', 'task': task})

# Delete a task
def delete_task(request, id):
    task = get_object_or_404(Task, id=id)  # Get task by id or return 404

    if request.method == 'POST':
        task.delete()  # Delete the task
        return redirect('index')  # Redirect to the task list page

    return render(request, 'task_confirm_delete.html', {'task': task})

# Filter tasks (e.g., by status)
def filter_tasks(request):
    status_filter = request.GET.get('status')  # Get the status filter from the query string
    if status_filter:
        tasks = Task.objects.filter(status=status_filter)  # Filter tasks based on status
    else:
        tasks = Task.objects.all()  # No filter, return all tasks

    return render(request, 'tasks_list.html', {'tasks': tasks})
