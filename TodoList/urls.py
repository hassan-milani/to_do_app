from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('todo', views.todo, name='todo'),
    path('delete-todo/<int:todo_id>', views.delete_todo, name='delete-todo')
]

