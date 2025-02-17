from django.urls import path
from tasks.views import manager_dashboard,user_dashboard,creat_task,view_task,update_task

urlpatterns = [
    path('manager-dashboard',manager_dashboard,name='manager-dashboard'),
    path('user-dashboard',user_dashboard),
    path('Create Task',creat_task),
    path('Create Task',creat_task,name='create_task'),
    path('view task',view_task),
    path('update-task/<int:id>/',update_task,name= 'updated_task'),
]
