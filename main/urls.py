from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="home"),
    path('editor/', views.editor_page),
    path('solve/<question_id>', views.solve_page)
]
