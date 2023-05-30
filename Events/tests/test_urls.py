from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from Events.models import Event, Hall
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile


class EventsURLTest(TestCase):
    def setUp(self):
        self.hall = Hall.objects.create(name='Test Hall')
        image_path = settings.BASE_DIR / 'media' / 'images' / 'events' / 'astronautart.jpg'
        image_data = open(image_path, 'rb').read()
        image = SimpleUploadedFile('astronautart.jpg', image_data, content_type='image/jpeg')

        self.event = Event.objects.create(
            name='Test Event',
            image=image,
            from_date='2023-01-01',
            to_date='2023-01-05',
            price=10.00,
            about='Test About',
            hall_id=self.hall,
            popularity=1
        )

    def test_all_events_url(self):
        url = reverse('events:all_events')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'all_events.html')

    def test_event_url(self):
        url = reverse('events:event', args=[self.event.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'event.html')

    def test_favourite_event_url(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_login(user)
        url = reverse('events:favourite_event', args=[self.event.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)