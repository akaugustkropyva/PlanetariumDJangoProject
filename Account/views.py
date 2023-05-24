from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from User.models import Customer
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            try:
                customer = Customer.objects.get(name=username, email=email)
                user = User.objects.create_user(username=username, email=email, password=password)
                customer.user = user
                customer.save()
            except Customer.DoesNotExist:
                user = form.save()
                Customer.objects.create(user=user, name=form.cleaned_data.get("username"), email=form.cleaned_data.get("email"))
            login(request, user)
            username = form.cleaned_data.get("username")
            messages.success(request, "Вітаю " + username + "! Акаунт було успішно створено")
            return redirect("user:profile")
    return render(request, 'register.html', {"form": form})


def log_in(request):
    form = LoginForm(request.POST)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("user:profile")
        else:
            messages.info(request, "Ім'я або пароль неправильні!")
    return render(request, "login.html", {"form": form})


def log_out(request):
    logout(request)
    return redirect("account:login")
