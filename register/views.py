from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.http import HttpResponseRedirect

# Create your views here.
def signup_page(request):
    
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:        
        form = RegisterForm()
    return render(request, "register/pages/signup.html", {"form":form})


def register_page(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:        
        form = RegisterForm()
    return render(request, "register/pages/register.html", {"form":form})
def signout_page(request):
    logout(request)
    #path of the homepage(the page which shoves if the user did not login ever) here in the quotes 
    return render(request,"")
