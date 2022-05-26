from django.shortcuts import render

def home(request):
    return render(request, "todolist/home.html")

def calender(request):
    return render(request, "todolist/calendar.html")