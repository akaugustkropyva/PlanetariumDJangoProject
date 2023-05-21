from django.urls import path, re_path
from .views import all_events, event, filters

app_name = 'events'
urlpatterns = [
    path('', all_events, name='all_events'),
    path('<int:parameter>/', event, name='event'),
    re_path(r'^(?P<date>(2023-(0[1-9]|1[0-2])-0[1-9]|[1-2][0-9]|3[0-1]))/(?P<halls>(big|small|stary))/'
            r'(?P<sorting>(popularity|price))/$', filters)
]

