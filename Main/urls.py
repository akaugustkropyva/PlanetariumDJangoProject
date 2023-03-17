from django.urls import path
from .views import main, about_us, contacts

app_name = 'main'
urlpatterns = [
    path('', main, name='landing'),
    path('aboutus/', about_us, name='about_us'),
    path('contacts/', contacts, name='contacts'),

]