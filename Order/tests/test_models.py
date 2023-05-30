from django.contrib.auth.models import User
from django.test import TestCase
from Events.models import Event, Hall
from User.models import Customer
from Order.models import Order, OrderItem


class OrderModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser')
        self.customer = Customer.objects.create(user=self.user, name='Test', phone='1234567890', email='test@example.com')
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
        self.order = Order.objects.create(customer=self.customer, complete=False, total=20.0)

    def test_order_str(self):
        self.assertEqual(str(self.order), str(self.order.id))

    def test_get_cart_total(self):
        order_item1 = OrderItem.objects.create(order=self.order, event=self.event, quantity=2)
        order_item2 = OrderItem.objects.create(order=self.order, event=self.event, quantity=3)
        expected_total = self.event.price * (order_item1.quantity + order_item2.quantity)
        self.assertEqual(self.order.get_cart_total, expected_total)

    def test_get_cart_items(self):
        order_item1 = OrderItem.objects.create(order=self.order, event=self.event, quantity=2)
        order_item2 = OrderItem.objects.create(order=self.order, event=self.event, quantity=3)
        expected_items = order_item1.quantity + order_item2.quantity
        self.assertEqual(self.order.get_cart_items, expected_items)


class OrderItemModelTest(TestCase):
    def setUp(self):
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

    def test_order_item_str(self):
        self.assertEqual(str(self.order_item), str(self.order_item.id))

    def test_get_total(self):
        expected_total = self.event.price * self.order_item.quantity
        self.assertEqual(self.order_item.get_total, expected_total)
