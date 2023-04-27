from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup_page),
    path("register/", views.register_page)
]