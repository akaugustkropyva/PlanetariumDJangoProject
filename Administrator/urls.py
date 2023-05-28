from django.urls import path
from .views import banusers, ban_user, unban_user, notallowed

app_name = 'administrator'
urlpatterns = [
    path('banusers/', banusers, name='banusers'),
    path('ban-user/<int:user_id>/', ban_user, name='ban_user'),
    path('unban-user/<int:user_id>/', unban_user, name='unban_user'),
    path('notallowed/', notallowed, name='notallowed')
]

