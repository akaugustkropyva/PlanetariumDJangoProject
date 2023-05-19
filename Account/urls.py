from django.urls import path, include
from .views import register, log_in

app_name = 'account'
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', log_in, name='login'),
]
