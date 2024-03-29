from django.shortcuts import render

from Events.models import Event
from .decorators import admin_only
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User

from .forms import EventForm


@admin_only
def banusers(request):
    users = User.objects.all()
    return render(request, 'banusers.html', context={'users': users})


@admin_only
def ban_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.banstatus.is_banned = True
    user.banstatus.save()
    return redirect('administrator:banusers')


@admin_only
def unban_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.banstatus.is_banned = False
    user.banstatus.save()
    return redirect('administrator:banusers')


@admin_only
def event_change(request, parameter):
    event = Event.objects.get(id=parameter)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
    else:
        form = EventForm(instance=event)

    return render(request, "event_form.html", {"form": form, "event": event})


@admin_only
def event_delete(request, parameter):
    event = Event.objects.get(id=parameter)
    event.delete()
    return redirect('events:all_events')


@admin_only
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('events:all_events')
    else:
        form = EventForm()
    return render(request, 'event_form.html', {'form': form})


def notallowed(request):
    return render(request, 'notallowed.html')
