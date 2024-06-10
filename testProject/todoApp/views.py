from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, TodoItemForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import TodoItem

# Create your views here.


@login_required
def base(request):
    context = {
        "name": "Ankit",
    }
    return render(request, "todoApp/base.html", context)


@login_required
def todo_list(request):
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            todo_item = form.save(commit=False)
            todo_item.user = request.user
            todo_item.save()
            return redirect('todo_list')
    else:
        form = TodoItemForm()

    items = TodoItem.objects.filter(user=request.user)
    return render(request, 'todoApp/todoShow.html', {'form': form, 'items': items})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'todoApp/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todo_list')
        else:
            return render(request, 'todoApp/login.html', {'error': 'Invalid credentials'})
    return render(request, 'todoApp/login.html')


def logout(request):

    return redirect('login')
