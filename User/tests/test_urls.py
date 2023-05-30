from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from User.models import Customer


class UserURLTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.customer = Customer.objects.create(user=self.user)

    def test_profile_url(self):
        url = reverse('user:profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user.html')

    def test_profile_change_url(self):
        self.client.force_login(self.user)
        url = reverse('user:profile_change')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_change.html')
