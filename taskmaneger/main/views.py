from django.shortcuts import render
from .models import Task


def index(request):
    tasks = Task.objects.order_by('id')
    return render(request, 'main/index.html', {'title': 'BookMaster', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')
