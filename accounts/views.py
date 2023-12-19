from django.shortcuts import render, redirect
from accounts.forms import LoginForm
from django.contrib.auth import login, logout, authenticate

def signin(request):
    if request.method =="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect("list_projects")
            else:
                form.add_error("username", "Invalid credentials")

    else:
        form = LoginForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)

def signout(request):
    logout(request)

    return redirect("login")
