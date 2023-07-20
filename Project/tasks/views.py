from django.shortcuts import render, redirect
from .models import Task

def index(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        status = request.POST.get('status')
        Task.objects.create(title=title, description=description, due_date=due_date, status=status)
        return redirect('index')
    return render(request, 'create.html')



def task_update(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.save()
        return redirect('index')
    return render(request, 'update.html', {'task': task})

def task_delete(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('index')
