from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def adminpage(request):
    return HttpResponse("<h1>Admin Page<h1>")
