from django.urls import path
from .views import user, history, order_info, wishlist

app_name = 'user'
urlpatterns = [
    path('', user, name='profile'),
    path('history/', history),
    path('history/<int:parameter>/', order_info),
    path('wishlist/', wishlist)
]
