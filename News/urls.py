from django.urls import path
from .views import all_news, news

app_name = 'news'
urlpatterns = [
    path('', all_news, name='all_news'),
    path('<int:parameter>/', news)
]