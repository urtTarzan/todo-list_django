from .models import Todo
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404,redirect



class TodoListView(ListView):
    model = Todo

class TodoCreatView(CreateView):
    model = Todo
    fields = ['title','deadline']
    success_url = reverse_lazy("todo_list")

class TodoUpdateView(UpdateView):
    model = Todo
    fields = ['title','deadline']
    success_url = reverse_lazy("todo_list")

class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")

class TodoCompleteView(View):
    def get(sef, request, pk):
        todo = get_object_or_404(Todo,pk=pk)
        Todo.mark_completed()
        return redirect("todo_list")
    