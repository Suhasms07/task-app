from django.db import models

class Task(models.Model):
    entity_name = models.CharField(max_length=100)  # Name of the customer
    task_type = models.CharField(max_length=50)  # Type of the task
    task_time = models.TimeField()  # Time when the task is scheduled
    contact_person = models.CharField(max_length=100,default=0)  # Person responsible for the task
    note = models.TextField(blank=True, null=True)  # Optional note for the task
    STATUS_CHOICES = [
        ('open', 'Open'),  # Default status when the task is created
        ('closed', 'Closed'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open')  # Task status (open/closed)

    def _str_(self):
        return f"{self.entity_name} - {self.task_type} - {self.status}"
