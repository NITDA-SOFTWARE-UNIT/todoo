from django.urls import path
from .views import *

urlpatterns = [
    path('todos/', CreateTodo.as_view(), name = 'create-todo'),
    path('todos/getall', ListTodo.as_view(), name = 'get-todo'),
    path('todos/<int:pk>/', DetailTodo.as_view(), name = 'single-todo'),
    path('todos/delete/<int:pk>/', DeleteTodo.as_view(), name = 'delete-todo'),
]