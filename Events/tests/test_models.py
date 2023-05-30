from django.test import TestCase
from django.contrib.auth.models import User
from Events.models import Hall, Event
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings


class HallModelTest(TestCase):
    def setUp(self):
        self.hall = Hall.objects.create(name='Test Hall')

    def test_str_representation(self):
        self.assertEqual(str(self.hall), 'Test Hall')


class EventModelTest(TestCase):
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
        self.event.favourite.add(self.user)

    def test_str_representation(self):
        self.assertEqual(str(self.event), 'Test Event')

    def test_favourite_users(self):
        self.assertEqual(list(self.event.favourite.all()), [self.user])

    def test_favourite_event(self):
        self.event.favourite.remove(self.user)
        self.assertFalse(self.event.favourite.filter(id=self.user.id).exists())

    def test_hall_related_name(self):
        self.assertEqual(self.event.hall_id, self.hall)
