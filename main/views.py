from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_page(response):
    return render (response, 'main/pages/home.html')

def editor_page(response):
    return render (response, 'main/pages/editor.html')