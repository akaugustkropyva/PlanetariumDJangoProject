from django.urls import path
from .views import all_events, event, favourite_event

app_name = 'events'
urlpatterns = [
    path('', all_events, name='all_events'),
    path('<int:parameter>/', event, name='event'),
    path('<int:parameter>/favourite_event', favourite_event, name='favourite_event'),
]

