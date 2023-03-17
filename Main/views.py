from django.http import HttpResponse
from django.shortcuts import render
from .models import Info, Proposal
from Events.models import Event

# Create your views here.

def main(request):
    # return HttpResponse("<h1>Planetarium<h1>")
    info = Info.objects.all()
    proposal = Proposal.objects.all()
    events = Event.objects.all()[:4]
    return render(request, "main.html", context={'info': info, 'proposal': proposal, 'events': events})


def about_us(request):
    return HttpResponse(f"<h1>About Us<h1>")


def contacts(request):
    return HttpResponse(f"<h1>Contacts<h1>")
