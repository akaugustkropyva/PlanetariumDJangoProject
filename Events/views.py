from django.http import HttpResponse
from django.shortcuts import render
from .models import Event


def filters(request, date: str, halls: str, sorting: str):
    return HttpResponse(f"<h1>All events filtered by {date}, {halls}, {sorting}<h1>")


def all_events(request):
    events = Event.objects.all()
    sorting = request.GET.get('sorting', '')
    search_query = request.GET.get('search', '')
    date_picker = request.GET.get('date', '')
    # print(date_picker)
    if search_query is not None and search_query != ' ':
        events = events.filter(name__icontains=search_query)
    if sorting:
        events = events.order_by(sorting)
    if date_picker:
        print(events.get('from_date'))
        events = events.filter(date_picker__range=('from_date', 'to_date'))

    return render(request, "all_events.html", context={'events': events})


def event(request, parameter):
    eventname = Event.objects.get(id=parameter)
    return render(request, "event.html", context={'event': eventname})
