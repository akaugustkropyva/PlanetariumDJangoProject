from django.http import HttpResponse
from django.shortcuts import render
from .models import Info, Proposal
from Events.models import Event


def main(request):
    info = Info.objects.all()
    proposal = Proposal.objects.all()
    events = Event.objects.all()[:4]
    return render(request, "main.html", context={'info': info, 'proposal': proposal, 'events': events})


def about_us(request):
    return render(request, "aboutus.html")


def contacts(request):
    return render(request, "contacts.html")
