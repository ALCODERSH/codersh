from django.shortcuts import render
from django.http import HttpResponse
from .models import Language, AceTheme, AceFont, Question
# Create your views here.


def home_page(response):
    return render(response, 'main/pages/home.html')


def editor_page(response):
    languages = Language.objects.all()
    themes = AceTheme.objects.all()
    fonts = AceFont.objects.all()
    questions = Question.objects.all()
    return render(response, 'main/pages/editor.html',
                  {
                      "languages": languages,
                      "themes": themes,
                      "fonts": fonts,
                      "questions": questions
                  }
                  )
