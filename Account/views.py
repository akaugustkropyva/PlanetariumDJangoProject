from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def register(request):
    return HttpResponse("<h1>Register<h1>")


def login(request):
    return HttpResponse(f"<h1>Login<h1>")

