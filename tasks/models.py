from django.db import models

# Create your models
class employee(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.name

class Task(models.Model):
    project = models.ForeignKey("Project",on_delete=models.CASCADE,default=1)
    assigned_to = models.ManyToManyField(employee)
    title = models.CharField(max_length = 250)
    description = models.TextField()
    due_date = models.DateField()
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
    task = models.OneToOneField(
        Task,
        on_delete=models.CASCADE,
        related_name='details'
        )
    assigned_to = models.CharField(max_length=100)
    priority = models.CharField(
        max_length=1,choices=priority_options,default=low
    )
class Project(models.Model):
    name = models.CharField(max_length=100)
    str_date = models.DateField()
