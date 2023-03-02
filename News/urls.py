from django.urls import path
from .views import all_news, news

urlpatterns = [
    path('', all_news),
    path('<int:parameter>/', news)
]