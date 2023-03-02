from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def main(request):
    return HttpResponse("<h1>Planetarium<h1>")


def about_us(request):
    return HttpResponse(f"<h1>About Us<h1>")


def contacts(request):
    return HttpResponse(f"<h1>Contacts<h1>")
