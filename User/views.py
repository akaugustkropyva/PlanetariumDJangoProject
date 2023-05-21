from django.http import HttpResponse
from django.shortcuts import render
from .forms import CustomerForm


def user(request):
    return render(request, "user.html")


def user_change(request):
    customer = request.user.customer
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            if form.cleaned_data['delete_photo']:
                customer.profile_pic.delete()
                customer.profile_pic = 'images/default_user.jpg'
            form.save()
    else:
        form = CustomerForm(instance=customer)

    return render(request, "user_change.html", {"form": form})


def history(request):
    return HttpResponse("<h1>History<h1>")


def order_info(request, parameter):
    request.parameter = parameter
    return HttpResponse(f"<h1>Order info {parameter}<h1>")


def wishlist(request):
    return HttpResponse("<h1>User's wishlist<h1>")
