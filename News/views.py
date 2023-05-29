from django.shortcuts import render
from .models import News


def all_news(request):
    news = News.objects.all()
    return render(request, "news.html", context={'news': news})

