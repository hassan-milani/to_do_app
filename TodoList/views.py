from django.shortcuts import render
from . import models
from django.utils import timezone
from django.http import HttpResponseRedirect

# Create your views here.


def home(request):
    todo_items = models.Todo.objects.all().order_by("-added_date")
    final_items = todo_items.values()
    stuff_for_frontend = {
        'todo_items': todo_items,
        'final_items': final_items,

    }
    return render(request, 'my_app/itemsview.html', stuff_for_frontend)


def todo(request):
    current_date = timezone.now()
    content = request.POST["content"]
    models.Todo.objects.create(added_date=current_date, item=content)
    todo_items = models.Todo.objects.all().order_by("-added_date")
    final_items = todo_items.values()
    stuff_for_frontend = {
        'todo_items': todo_items,
        'final_items': final_items,

    }
    return render(request, 'my_app/itemsview.html', stuff_for_frontend)


def delete_todo(request, todo_id):
    models.Todo.objects.get(id=todo_id).delete()
    print(models.Todo.objects.all())
    return HttpResponseRedirect("/TodoList")


