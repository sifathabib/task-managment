from django.db import models

# Create your models
class Task(models.Model):
    title = models.CharField(max_length = 250)
    description = models.TextField()
    due_date = models.DateTimeField()
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class TaskDetail(models.Model):
    high ='H'
    medium = 'M'
    low = 'L'
    priority_options = (
        (high,'High'),
        (medium,'Medium'),
        (low,'Low')
    )
    task = models.OneToOneField(Task,on_delete=models.CASCADE)
    assigned_to = models.CharField(max_length=100)
    priority = models.CharField(
        max_length=1,choices=priority_options,default=low
    )