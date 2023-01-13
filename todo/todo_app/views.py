from django.shortcuts import render, redirect
from django.urls import include
from .form import ToDoForms
from .models import Task

def Tasks(request):
    task1=Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,'task.html',{'tasks':task1})
def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')

    return render(request,'delete.html')
def update(request,id):
    task=Task.objects.get(id=id)
    form=ToDoForms(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form ,'task':task})

