# registration/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('welcome/<str:role>/', views.welcome, name='welcome'),  # Добавляем URL-шаблон для страницы приветствия
]
