from django.shortcuts import render
from django.http import HttpResponse

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
            "names" : names,
            "age": 29,
            "count" : count
        }
        return render(request,"test.html",context)
