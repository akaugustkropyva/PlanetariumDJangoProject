from django.urls import path
from .views import cart

app_name = 'order'
urlpatterns = [
    path('cart/', cart, name='cart')
]
