from django.urls import path
from .views import user, history, order_info, wishlist

urlpatterns = [
    path('', user),
    path('history/', history),
    path('history/<int:parameter>/', order_info),
    path('wishlist/', wishlist)
]
