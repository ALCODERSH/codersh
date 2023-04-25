from django.shortcuts import render
from django.http import HttpResponse
from .models import Language
# Create your views here.
def home_page(response):
    return render (response, 'main/pages/home.html')

def editor_page(response):
    lang = Language.objects.all()
    return render (response, 'main/pages/editor.html', {"lang":lang})