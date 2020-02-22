from django.contrib.auth import (
authenticate,
get_user_model,
login,
logout
)
from django.shortcuts import render, redirect
from .forms import UserLoginForm,UserRegisterForm

def login_view(request):

    title = "Login Form"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("/home")
    context = {"form": form,
               "title": title
               }
    return render(request,"form.html",context)

def register_view(request):
    print(request.user.is_authenticated())
    title = "Register Form"
    form = UserRegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        #redirect
        return redirect("/")

    context = {"form":form,
               "title": title
               }
    return render(request,"form.html",context)

def logout_view(request):
    logout(request)
    return redirect("/login")