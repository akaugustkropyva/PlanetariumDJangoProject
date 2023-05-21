from django.http import HttpResponse
from django.shortcuts import render


def cart(request):
    return render(request, "cart.html")
