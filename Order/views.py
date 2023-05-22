from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from Events.models import Event
from Order.models import Order, OrderItem
import json


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'det_cart_total': 0}
        cartItems = order['get_cart_total']
    return render(request, "cart.html", {'items': items, 'order': order})


def updateItem(request):
    data = json.loads(request.body)
    eventId = data['eventId']
    action = data['action']

    print('Action:', action)
    print('eventId:', eventId)

    customer = request.user.customer
    event = Event.objects.get(id=eventId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, event=event)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)
