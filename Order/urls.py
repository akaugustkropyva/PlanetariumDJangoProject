from django.urls import path
from .views import cart, updateItem

app_name = 'order'
urlpatterns = [
    path('cart/', cart, name='cart'),
    path('update_item/', updateItem, name='update_item')
]
