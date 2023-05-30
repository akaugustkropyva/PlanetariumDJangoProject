from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from User.models import Customer
from Order.models import Order, OrderItem
from Events.models import Event, Hall


class UpdateItemViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser')
        self.customer = Customer.objects.create(user=self.user, name='Test', phone='1234567890',
                                                email='test@example.com')
        self.hall = Hall.objects.create(name='Test Hall')

        self.event = Event.objects.create(
            name='Test Event',
            image='path/to/image.jpg',
            from_date='2023-01-01',
            to_date='2023-01-05',
            price=10.00,
            about='Test About',
            hall_id=self.hall,
            popularity=1
        )
        self.order = Order.objects.create(complete=False, total=20.0)
        self.order_item = OrderItem.objects.create(order=self.order, event=self.event, quantity=2)
        self.url = reverse('order:update_item')
        self.data = {
            'eventId': self.event.id,
            'eventDate': '2023-05-28',
            'action': 'add',
        }

    def test_update_item_authenticated_user(self):
        self.client.force_login(self.customer.user)
        response = self.client.post(self.url, data=self.data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 'Cart was changed')
        self.order_item.refresh_from_db()
        self.assertEqual(self.order_item.quantity, 2)

