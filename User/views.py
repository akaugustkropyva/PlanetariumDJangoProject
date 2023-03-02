from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def user(request):
    return HttpResponse("<h1>User<h1>")


def history(request):
    return HttpResponse("<h1>History<h1>")


def order_info(request, parameter):
    request.parameter = parameter
    return HttpResponse(f"<h1>Order info {parameter}<h1>")


def wishlist(request):
    return HttpResponse("<h1>User's wishlist<h1>")
