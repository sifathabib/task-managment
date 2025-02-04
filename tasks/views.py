from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import Task,TaskModelForm
from tasks.models import employee,Task

def manager_dashboard(request):
    return render(request,"dashboard/manager-dashboard.html")

def user_dashboard(request):
    return render(request,"dashboard/user-dashboard.html")
def sifat_page(request):
    return HttpResponse("<h1>hello sifat how are you</h1>")
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

