from django.urls import path
from tasks.views import manager_dashboard,user_dashboard,math_academy,creat_task

urlpatterns = [
    path('manager-dashboard',manager_dashboard),
    path('user-dashboard',user_dashboard),
    path('math-acadey',math_academy),
    path('Create Task',creat_task)
]
