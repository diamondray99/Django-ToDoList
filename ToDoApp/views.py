from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import *
from .forms import *


# Create your views here.


def index(request):
    todo_list = ToDoModel.objects.order_by('id')
    form = newTodo()
    context = {
        'todo_list': todo_list,
        'form': form,
    }
    return render(request, template_name='index.html', context=context)


@require_POST
def addTodo(request):
    form = newTodo(request.POST)
    if form.is_valid():
        new_todo = ToDoModel(text=form.cleaned_data['text'])
        new_todo.save()
    return redirect('index')


def completeTodo(request, todo_id):
    todo = ToDoModel.objects.get(id=todo_id)
    todo.complete = True
    todo.save()
    return redirect('index')


def deleteCompleted(request):
    ToDoModel.objects.filter(complete__exact=True).delete()
    return redirect('index')


def delete(request):
    ToDoModel.objects.all().delete()
    return redirect('index')
