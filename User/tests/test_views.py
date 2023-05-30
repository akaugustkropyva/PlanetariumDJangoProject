from User.models import Customer
from User.forms import CustomerForm
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse


class UserViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('user:profile')

    def test_user_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user.html')


class UserChangeViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser')
        self.customer = Customer.objects.create(user=self.user)
        self.url = reverse('user:profile_change')

    def test_user_change_get_request(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], CustomerForm)
        self.assertTemplateUsed(response, 'user_change.html')

