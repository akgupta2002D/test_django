from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

# Create your views here.


def base(request):
    context = {
        "name": "Ankit",
    }
    return render(request, "todoApp/base.html", context)


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
            return redirect('base')
        else:
            return render(request, 'todoApp/login.html', {'error': 'Invalid credentials'})
    return render(request, 'todoApp/login.html')


def logout(request):

    return redirect('login')
