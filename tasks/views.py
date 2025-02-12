from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import Task,TaskModelForm
from tasks.models import Employee,Task,Project,TaskDetail
from django.db.models import Q, Count, Max, Min, Avg,Sum
from datetime import date
def manager_dashboard(request):
    tasks= Task.objects.all()
    total_tasks = tasks.count()
    completed_task = Task.objects.filter(status = "COMPLETED").count()
    in_progress_task  = Task.objects.filter(status = "IN_PROGRESS").count()
    pending_task = Task.objects.filter(status="PENDING").count()

    counts = {
        "tasks":tasks,
        "total_task":total_tasks,
        "completed_task":completed_task,
        "in_progrss":in_progress_task,
        "pending_task":pending_task

    }
    return render(request,"dashboard/manager-dashboard.html",counts)



def user_dashboard(request):
    return render(request,"dashboard/user-dashboard.html")

def math_academy(request):
    names = ["sifat","siam","shihab","shibli"]
    count = 0
    for name in names:
        count =count+1
        context = {
            "names" : name,
            "age": 29,
            "count" : count
        }
        return render(request,"test.html",context)
def creat_task(request):
    # employees = employee.objects.all()
    # form = TaskForm(employees = employees)
    form = TaskModelForm()

    if request.method == "POST":
        form = TaskModelForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'task_form.html',{"forms":form,"massage":"task added successfully"})
            # data =form.cleaned_data
            # print("form is valid",data)
            # title = data.get('title')
            # description = data.get('description')
            # due_date = data.get('due_date')
            # assigned_to = data.get('assigned_to')

            # task = Task.objects.create(title=title,description=description,due_date= due_date)
            # print("Task Created")

            # for emp_id in assigned_to:
            #     emp = employee.objects.get(id=emp_id)
            #     task.assigned_to.add(emp)
            # return HttpResponse("Task added successfully")
    context = {"forms":form}
    return render(request,"task_form.html",context)
def view_task(request):
    task = Task.objects.all()
    task1 = Project.objects.all()
    task2 = Task.objects.filter(status="IN_PROGRESS")
    today = date.today
    task3= Task.objects.filter(due_date=date.today())
    task4= TaskDetail.objects.all()
    task4= TaskDetail.objects.filter(priority ="H")
    task5=Task.objects.filter(title__icontains = "a",status = "PENDING")

    task6=Task.objects.select_related('details').all()
    task7 = TaskDetail.objects.select_related('task').all() 

    task8 = Task.objects.aggregate(
                                    total = Count('id'),
                                    due_date = Max('due_date'),
                                    
                                   
                                   )
   

    employees = Employee.objects.annotate(total_tasks=Count('tasks')).order_by('total_tasks')

   
 
   
    return render(request,"show_task.html",{"tasks":task,"task1":task1,"task2":task2,"task3":task3,"task4":task4,"task5":task5,"task6":task6,"task7":task7,"task8":task8,"task9":employees})
    





