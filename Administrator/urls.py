from django.urls import path
from .views import banusers, ban_user, unban_user, notallowed, event_change, event_create, event_delete

app_name = 'administrator'
urlpatterns = [
    path('banusers/', banusers, name='banusers'),
    path('ban-user/<int:user_id>/', ban_user, name='ban_user'),
    path('unban-user/<int:user_id>/', unban_user, name='unban_user'),
    path('notallowed/', notallowed, name='notallowed'),
    path('event-create/', event_create, name='event_create'),
    path('<int:parameter>/event-change/', event_change, name='event_change'),
    path('<int:parameter>/delete/', event_delete, name='even_delete'),
]

