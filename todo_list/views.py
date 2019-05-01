from django.shortcuts import render, get_object_or_404, redirect
from .models import TodoList
from .forms import TodoForm

def todo_list(request):
	todo = TodoList.objects.all()
	return render(request, 'todo_list/todo_list.html', {'todo': todo})

def TodoNew(request):
	if request.method == "POST":
		form = TodoForm(request.POST)
		if form.is_valid():
			todo = form.save(commit=False)
			todo.save()
			return redirect('Detail_list', pk=todo.pk)
	else:
		form = TodoForm()
	return render(request, 'todo_list/Edit_list.html', {'form': form})

def Detail_list(request, pk):
	todo = get_object_or_404(TodoList, pk=pk)
	return render(request, 'todo_list/Detail_list.html', {'todo': todo})


def Edit_list(request, pk):
	todo = get_object_or_404(TodoList, pk=pk)
	if request.method == "POST":
		form = TodoForm(request.POST, instance=todo)
		if form.is_valid():
			todo = form.save(commit=False)
			todo.save()
			return redirect('Detail_list', pk=todo.pk)
	else:
		form = TodoForm(instance=todo)
	return render(request, 'todo_list/Edit_list.html', {'form': form})