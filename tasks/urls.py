from django.urls import path
from tasks.views import manager_dashboard,user_dashboard,creat_task,view_task 

urlpatterns = [
    path('manager-dashboard',manager_dashboard),
    path('user-dashboard',user_dashboard),
    path('Create Task',creat_task),
    path('view task',view_task)
]
