from django.test import TestCase
from django.urls import reverse
from News.models import News
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile


class NewsURLTest(TestCase):
    def setUp(self):
        image_path = settings.BASE_DIR / 'media' / 'images' / 'news' / 'mars.jpg'
        image_data = open(image_path, 'rb').read()
        image = SimpleUploadedFile('mars.jpg', image_data, content_type='image/jpeg')
        self.news = News.objects.create(
            name='Test News',
            image=image,
            about='Test About',
            link='https://example.com'
        )

    def test_all_news_url(self):
        url = reverse('news:all_news')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
