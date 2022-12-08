from django.shortcuts import render
from .models import Task


def index(request):
    # task = Task.objects.all()
    task = Task.objects.order_by('-id') # [1], по id
    return render(request, 'main/index.html', {'title': 'главный текст', 'tasks': task})


def about(request):
    return render(request, 'main/about.html')
