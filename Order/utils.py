from Events.models import Event
import json


def cookieCard(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
        print(cart)
    except:
        cart = {}

    items = []
    order = {'get_cart_total': 0, 'get_cart_items': 0}

    for i in cart:
        print(i)
        try:
            event = Event.objects.get(id=i)
            for date in cart[i]:
                print(date)
                total = (event.price * cart[i][date]['quantity'])

                order['get_cart_total'] += total
                order['get_cart_items'] += cart[i][date]['quantity']

                item = {
                    'event': {
                        'id': event.id,
                        'name': event.name,
                        'image': event.image,
                        'price': event.price,
                    },
                    'quantity': cart[i][date]['quantity'],
                    'date_event': date,
                    'get_total': total,
                }
                items.append(item)
        except:
            pass
    print(items)
    return {'items': items, 'order': order}
