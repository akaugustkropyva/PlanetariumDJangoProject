from django.http import JsonResponse
from django.shortcuts import render
from Events.models import Event
from Order.models import Order, OrderItem
from Administrator.decorators import admin_not_allowed
from .forms import OrderForm
from User.models import Customer
from .utils import cookieCard
import json
import datetime


@admin_not_allowed
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        cookieData = cookieCard(request)
        order = cookieData['order']
        items = cookieData['items']
    return render(request, "cart.html", {'items': items, 'order': order})


@admin_not_allowed
def submit(request):
    form_validated = False
    customer = None

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        form = OrderForm(instance=customer)
    else:
        cookieData = cookieCard(request)
        order = cookieData['order']
        form = OrderForm()

    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form_validated = True
    return render(request, "submit.html", {'order': order, 'form': form, 'form_validated': form_validated})


@admin_not_allowed
def updateItem(request):
    data = json.loads(request.body)
    eventId = data['eventId']
    eventDate = data['eventDate']
    action = data['action']

    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    if eventId and eventDate:
        event = Event.objects.get(id=eventId)
        orderItem, created = OrderItem.objects.get_or_create(order=order, event=event, date_event=eventDate)

        if action == 'add':
            orderItem.quantity = (orderItem.quantity + 1)
        elif action == 'remove':
            orderItem.quantity = (orderItem.quantity - 1)
        elif action == 'delete-item':
            orderItem.quantity = 0

        orderItem.save()

        if orderItem.quantity <= 0:
            orderItem.delete()

    if action == 'delete-all':
        order.delete()

    return JsonResponse('Cart was changed', safe=False)


@admin_not_allowed
def procesOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

    else:
        name = data['form']['name']
        email = data['form']['email']
        phone = data['form']['phone']

        cookieData = cookieCard(request)
        items = cookieData['items']

        customer, created = Customer.objects.get_or_create(
            email=email,
        )
        customer.name = name
        customer.phone = phone

        customer.save()

        order = Order.objects.create(
            customer=customer,
            complete=False,
        )

        for item in items:
            event = Event.objects.get(id=item['event']['id'])

            orderItem = OrderItem.objects.create(
                event=event,
                order=order,
                quantity=item['quantity'],
                date_event=item['date_event'],
            )

    total = float(data['card']['total'])
    card_number = float(data['card']['card_number'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
        order.total = total
        order.card_number = card_number
    order.save()

    return JsonResponse('Payment complete!', safe=False)
