from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from Events.models import Event, Hall


class EventViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
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

    def test_all_events_view(self):
        url = reverse('events:all_events')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'all_events.html')
        self.assertContains(response, self.event.name)

    def test_event_view(self):
        url = reverse('events:event', args=[self.event.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'event.html')
        self.assertEqual(response.context['event'], self.event)
        self.assertFalse(response.context['is_favourite'])

    def test_favourite_event_view(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('events:favourite_event', args=[self.event.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(self.event.favourite.filter(id=self.user.id).exists())
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(self.event.favourite.filter(id=self.user.id).exists())
