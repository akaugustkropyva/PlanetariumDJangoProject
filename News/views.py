from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def all_news(request):
    return HttpResponse("<h1>All news<h1>")


def news(request, parameter: int):
    return HttpResponse(f"<h1>News {parameter}<h1>")

