from django.urls import path
from . import views

urlpatterns = [
    path('rezka_films/', views.RezkaListView.as_view()),
    path('manas_films/', views.ManasListView.as_view()),
    path('film_parser/', views.GetParsing.as_view()),
]