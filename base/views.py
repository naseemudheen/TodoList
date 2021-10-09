from django.shortcuts import render,redirect,get_object_or_404
from .forms import TaskForm
from .models import Task
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    context = {}
    context['tasks'] = Task.objects.filter(user=request.user).order_by("completed")
    context['count'] = context['tasks'].filter(completed=False).count()
    return render(request,'base/home.html',context)

@login_required
def createTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        
        if form.is_valid():
            form = form.save(commit =False)
            form.user = request.user
            form.save()
            return redirect('home')
    else:
        form = TaskForm()
    context = {
        'form' : form
    }
    return render(request,'base/task_form.html',context)

@login_required
def viewTask(request,id):
    context = {}
    context['task'] = Task.objects.get(id =id )
    return render(request,'base/task.html',context)

@login_required
def deleteTask(request,id):
    context = {}
    obj = get_object_or_404(Task, id = id)
    if request.method =='POST':
        obj.delete()
        return redirect('home')
    return render(request,'base/delete_task.html',context)

@login_required
def completeTask(request,id):
    Task.objects.filter(id = id).update(completed = True)
    return redirect('home')

@login_required
def incompleteTask(request,id):
    Task.objects.filter(id = id).update(completed = False)
    return redirect('home')



def register(request):
    if request.method =='POST':
        form =UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm() 
    return render(request,'registration/register.html',{'form':form})
