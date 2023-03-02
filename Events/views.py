from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def filters(request, date: str, halls: str, sorting: str):
    return HttpResponse(f"<h1>All events filtered by {date}, {halls}, {sorting}<h1>")


def all_events(request):
    return HttpResponse("<h1>All events<h1>")


def event(request, parameter: int):
    return HttpResponse(f"<h1>Event {parameter}<h1>")
