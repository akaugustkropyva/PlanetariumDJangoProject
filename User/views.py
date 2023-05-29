from django.shortcuts import render
from Administrator.decorators import allowed_users
from Order.models import Order
from .forms import CustomerForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


@login_required(login_url='account:login')
def user(request):
    return render(request, "user.html")


@login_required(login_url='account:login')
def user_change(request):
    customer = request.user.customer
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            if form.cleaned_data['delete_photo']:
                if customer.profile_pic != 'images/default_user.jpg':
                    customer.profile_pic.delete()
                    customer.profile_pic = 'images/default_user.jpg'
            form.save()
    else:
        form = CustomerForm(instance=customer)

    return render(request, "user_change.html", {"form": form})


@login_required(login_url='account:login')
@allowed_users(allowed_roles=['customer'])
def history(request):
    customer = request.user.customer
    orders = Order.objects.filter(customer=customer)
    reversed_orders = reversed(orders)
    return render(request, "history.html", {"orders": orders, "reversed_orders": reversed_orders})


@login_required(login_url='account:login')
@allowed_users(allowed_roles=['customer'])
def order_info(request, parameter):
    order = Order.objects.get(id=parameter)
    items = order.orderitem_set.all()
    return render(request, "order_info.html", context={'order': order, 'items': items})


@login_required(login_url='account:login')
@allowed_users(allowed_roles=['customer'])
def wishlist(request):
    user = request.user
    favourite_event = user.favourite.all()
    paginator = Paginator(favourite_event, 4)

    page_number = request.GET.get('page')
    paginator_events = paginator.get_page(page_number)
    return render(request, "wishlist.html", context={'events': paginator_events})
