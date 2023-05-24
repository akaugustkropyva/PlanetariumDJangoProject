from django.urls import path
from .views import cart, updateItem, submit, procesOrder

app_name = 'order'
urlpatterns = [
    path('cart/', cart, name='cart'),
    path('submit/', submit, name='submit'),
    path('update_item/', updateItem, name='update_item'),
    path('proces_order/', procesOrder, name='proces_order')
]
