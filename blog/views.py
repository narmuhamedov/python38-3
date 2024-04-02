from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from blog.models import BlogNews


def post_news_view(request):
    if request.method == 'GET':
        query = BlogNews.objects.all()
        return render(request, template_name='news.html',
                      context={'query': query})


def post_news_detail_view(request, id):
    if request.method == 'GET':
        query_id = get_object_or_404(BlogNews, id=id)
        return render(request, template_name='news_detail.html',
                      context={'query_id': query_id})





def hello_world(request):
    if request.method == "GET":
        return HttpResponse(f"<h1>Привет этой мой первый запрос на DJANGO-TEMPLATES-{datetime.now()}</h1>")
