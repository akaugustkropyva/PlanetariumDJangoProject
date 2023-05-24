from django.urls import path
from .views import user, history, order_info, wishlist, user_change

app_name = 'user'
urlpatterns = [
    path('', user, name='profile'),
    path('change/', user_change, name='profile_change'),
    path('history/', history, name='history'),
    path('history/<int:parameter>/', order_info, name='order_info'),
    path('wishlist/', wishlist, name='wishlist')
]
