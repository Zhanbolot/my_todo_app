from django.urls import path
from . import views

urlpatterns = [
	path('', views.todo_list, name='todo_list'),
	path('todo/<int:pk>/', views.Detail_list, name='Detail_list'),
	path('todo/new/', views.TodoNew, name='TodoNew'),
	path('todo/<int:pk>/edit>', views.Edit_list, name='Edit_list'),
]