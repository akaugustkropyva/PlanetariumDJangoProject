from django.test import TestCase
from django.urls import reverse
from Main.models import Info, Proposal
from Events.models import Event, Hall


class MainViewTest(TestCase):
    def setUp(self):
        self.proposal = Proposal.objects.create(name='Test Proposal', image='path/to/image.jpg')
        self.info = Info.objects.create(text='Test Info', proposal_id=self.proposal)
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

    def test_main_view(self):
        response = self.client.get(reverse('main:landing'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        self.assertQuerysetEqual(response.context['info'], [self.info])
        self.assertQuerysetEqual(response.context['proposal'], [self.proposal])
        self.assertQuerysetEqual(response.context['events'], [self.event])


class AboutUsViewTest(TestCase):
    def test_about_us_view(self):
        response = self.client.get(reverse('main:about_us'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'aboutus.html')


class ContactsViewTest(TestCase):
    def test_contacts_view(self):
        response = self.client.get(reverse('main:contacts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contacts.html')
