from django.test import TestCase
from django.urls import reverse


class MainUrlsTestCase(TestCase):
    def test_main_url(self):
        url = reverse('main:landing')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_about_us_url(self):
        url = reverse('main:about_us')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_contacts_url(self):
        url = reverse('main:contacts')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
