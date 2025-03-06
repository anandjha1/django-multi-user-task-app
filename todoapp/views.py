from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.decorators import login_required
from .models import Task

# Create your views here.

@login_required
def index(request):
    tasks = Task.objects.filter(user = request.user)
    context = {
        'tasks': tasks
    }
    return render(request, 'index.html', context=context)

@login_required
def create_todo(request):
    if request.method == 'POST':
        task = Task.objects.create(title=request.POST.get('title'), user = request.user)
        task.save()

    return redirect('home')

@login_required
def update_todo(request, id):
    task = Task.objects.get(id=id, user = request.user)
    if request.method == 'POST':
        print(request.body)
        status = request.POST.get('completed', False) == 'on'
        task.title = request.POST.get('title', task.title)
        task.completed = status
        task.save()
        return redirect("home")
    
    context = {
        'task': task
    }
    return render(request, 'update.html', context=context)

@login_required
def delete_todo(request, id):
    task = Task.objects.get(id=id, user=request.user)
    task.delete()
    return redirect('home')