from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_page(response):
    return HttpResponse ("Home page")

def editor_page(response):
    return HttpResponse ("Editor Page")