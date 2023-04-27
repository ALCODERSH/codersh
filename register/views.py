from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup_page(request):
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("")
    else:        
        form = UserCreationForm()
    return render(request, "register/pages/signup.html", {"form":form})


def register_page(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("")
    else:        
        form = UserCreationForm()
    return render(request, "register/pages/register.html", {"form":form})