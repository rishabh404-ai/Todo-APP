from django.shortcuts import render, redirect
from .models import Todo
from .forms import todoform

# Create your views here.
def index(request):
    todo_list = Todo.objects.all()

    form = todoform()

    return render(request,'index.html', {'todo_list' : todo_list, 'form': form })


def addtodo(request):
    form = todoform(request.POST)

    if form.is_valid():
        new_todo=Todo(text=form.cleaned_data['text'])
        new_todo.save()

    return redirect('index') 

def completetodo(request, Todo_id):
    todo = Todo.objects.get(pk=Todo_id)
    todo.completed = True
    todo.save()
   
    return redirect('index')    

def deletecompleted(request):
    Todo.objects.filter(completed__exact=True).delete()
    return redirect('index')        

def deleteall(request):
    Todo.objects.all().delete()
    return redirect('index')    