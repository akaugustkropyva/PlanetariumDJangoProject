from django.test import TestCase, Client
from django.urls import reverse
from News.models import News


class NewsViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.news1 = News.objects.create(name='News 1', image='path/to/image1.jpg', about='About 1')
        self.news2 = News.objects.create(name='News 2', image='path/to/image2.jpg', about='About 2')

    def test_all_news_view(self):
        url = reverse('news:all_news')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news.html')
        self.assertCountEqual(response.context['news'], [self.news1, self.news2])
