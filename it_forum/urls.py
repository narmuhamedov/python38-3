from django.urls import path
from it_forum.views import (CreateAnswerView,
                            AnsewersListView,
                            AnswersDetailView,
                            DeleteAnswerView,
                            UpdateAnswerView,
                            SearchAnswerView,
                            CreateReviewView)


app_name = 'it_forum'
urlpatterns = [
    path('answer_list/', AnsewersListView.as_view()),
    path('answer_list/<int:id>/', AnswersDetailView.as_view(), name='detail'),
    path('answer_list/<int:id>/delete/', DeleteAnswerView.as_view()),
    path('answer_list/<int:id>/update/', UpdateAnswerView.as_view()),
    path('create_answer/', CreateAnswerView.as_view()),
    path('create_review/', CreateReviewView.as_view()),
    path('seacrh/', SearchAnswerView.as_view(), name='search'),
]
