from django.test import TestCase
from News.models import News


class NewsModelTest(TestCase):
    def setUp(self):
        self.news = News.objects.create(
            name='Test News',
            image='path/to/image.jpg',
            about='Test About',
            link='https://example.com'
        )

    def test_news_name(self):
        self.assertEqual(self.news.name, 'Test News')

    def test_news_image(self):
        self.assertEqual(self.news.image, 'path/to/image.jpg')

    def test_news_about(self):
        self.assertEqual(self.news.about, 'Test About')

    def test_news_link(self):
        self.assertEqual(self.news.link, 'https://example.com')

    def test_news_str(self):
        self.assertEqual(str(self.news), 'Test News')