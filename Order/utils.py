from Events.models import Event
import json


def cookieCard(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}

    items = []
    order = {'get_cart_total': 0, 'get_cart_items': 0}

    for i in cart:
        try:
            event = Event.objects.get(id=i)
            total = (event.price * cart[i]['quantity'])

            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]['quantity']

            item = {
                'event': {
                    'id': event.id,
                    'name': event.name,
                    'image': event.image,
                    'price': event.price,
                },
                'quantity': cart[i]['quantity'],
                'get_total': total,
            }
            items.append(item)
        except:
            pass
    return {'items': items, 'order': order}
