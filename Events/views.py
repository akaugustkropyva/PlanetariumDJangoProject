from django.http import HttpResponse
from django.shortcuts import render
from .models import Event


def filters(request, date: str, halls: str, sorting: str):
    return HttpResponse(f"<h1>All events filtered by {date}, {halls}, {sorting}<h1>")


def all_events(request):
    events = Event.objects.all()
    return render(request, "all_events.html", context={'events': events})


def event(request, parameter):
    event = Event.objects.get(id=parameter)
    return render(request, "event.html", context={'event': event})
