from django.shortcuts import render, redirect
from .models import Event


def all_events(request):

    search_query = request.GET.get('search', '')
    date_picker = request.GET.get('date', '')
    sorting = request.GET.get('sorting', '')

    if search_query is not None and search_query != ' ':
        events = Event.objects.filter(name__icontains=search_query)
    else:
        events = Event.objects.all()
    if date_picker:
        events = events.filter(from_date__lte=date_picker, to_date__gte=date_picker)
    if sorting:
        events = events.order_by(sorting)
    return render(request, "all_events.html", context={'events': events})


def event(request, parameter):
    event = Event.objects.get(id=parameter)
    is_favourite = False
    if event.favourite.filter(id=request.user.id).exists():
        is_favourite = True
    return render(request, "event.html", context={'event': event, "is_favourite": is_favourite})


def favourite_event(request, parameter):
    event = Event.objects.get(id=parameter)
    if event.favourite.filter(id=request.user.id).exists():
        event.favourite.remove(request.user)
    else:
        event.favourite.add(request.user)
    return redirect('events:event', parameter=parameter)
