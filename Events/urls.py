from django.urls import path, re_path
from .views import all_events, event, filters

urlpatterns = [
    path('', all_events),
    path('<int:parameter>/', event),
    re_path(r'^(?P<date>(0[1-9]|[1-2][0-9]|3[0-1])-(0[1-9]|1[0-2])-2023)/(?P<halls>(big|small|stary))/'
            r'(?P<sorting>(popularity|price))/$', filters)
]

