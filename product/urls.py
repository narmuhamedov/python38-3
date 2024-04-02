from django.urls import path
from . import views

urlpatterns = [
    path('all_product/', views.ProductListView.as_view()),
    path('meal/', views.MealListView.as_view()),
]

