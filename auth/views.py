from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .form import UserForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Login")
    context = {"form": form}
    return render(request, "SignIn.html", context)


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("Dashboard")
    return render(request, "Login.html")


def logout_view(request):
    logout(request)
    return redirect("Login")


@login_required(login_url="Login")
def Dashboard_view(request):
    return render(request, "Home.html")
