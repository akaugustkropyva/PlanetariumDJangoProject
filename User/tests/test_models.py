from django.test import TestCase
from django.contrib.auth.models import User
from User.models import Customer


class CustomerModelTest(TestCase):
    def test_customer_creation(self):
        user = User.objects.create_user(username='testuser')
        customer = Customer.objects.create(
            user=user,
            name='John Doe',
            phone='1234567890',
            email='john@example.com',
            profile_pic='path/to/profile_pic.jpg'
        )
        self.assertEqual(customer.user, user)
        self.assertEqual(customer.name, 'John Doe')
        self.assertEqual(customer.phone, '1234567890')
        self.assertEqual(customer.email, 'john@example.com')
        self.assertEqual(customer.profile_pic, 'path/to/profile_pic.jpg')
