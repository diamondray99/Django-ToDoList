from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('addtodo/', addTodo, name='addTodo'),
    path('completeTodo/<todo_id>', completeTodo, name='completeTodo'),
    path('deleteCompleted/', deleteCompleted, name='deleteCompleted'),
    path('delete/', delete, name='delete'),


]
