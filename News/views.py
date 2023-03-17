from django.http import HttpResponse
from django.shortcuts import render
from .models import News


def all_news(request):
    news = News.objects.all()
    return render(request, "news.html", context={'news': news})
    # return HttpResponse("<h1>All news<h1>")


def news(request, parameter: int):
    return HttpResponse(f"<h1>News {parameter}<h1>")
