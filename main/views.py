from django.shortcuts import render
from django.http import HttpResponse
from .models import Language, AceTheme, AceFont, Question
# Create your views here.


def home_page(request):
    return render(request, 'main/pages/home.html')


def editor_page(request):
    languages = Language.objects.all()
    themes = AceTheme.objects.all()
    fonts = AceFont.objects.all()
    questions = Question.objects.all()
    return render(request, 'main/pages/editor.html',
                  {
                      "languages": languages,
                      "themes": themes,
                      "fonts": fonts,
                      "questions": questions
                  }
                  )

def solve_page(request, question_id):
    languages = Language.objects.all()
    themes = AceTheme.objects.all()
    fonts = AceFont.objects.all()
    question = Question.objects.get(id=question_id)
    print(question)

    return render(
        request, 
        'main/pages/editor.html',
        {
            "languages": languages,
            "themes": themes,
            "fonts": fonts,
            "question": question
        }
    )