from django.test import SimpleTestCase
from django.urls import reverse, resolve
from Order.views import cart, updateItem, submit, procesOrder


class OrderURLTest(SimpleTestCase):
    def test_cart_url(self):
        url = reverse('order:cart')
        self.assertEqual(resolve(url).func, cart)

    def test_submit_url(self):
        url = reverse('order:submit')
        self.assertEqual(resolve(url).func, submit)

    def test_update_item_url(self):
        url = reverse('order:update_item')
        self.assertEqual(resolve(url).func, updateItem)

    def test_proces_order_url(self):
        url = reverse('order:proces_order')
        self.assertEqual(resolve(url).func, procesOrder)
