from django.urls import path
from .views import main, about_us, contacts

urlpatterns = [
    path('', main),
    path('aboutus/', about_us),
    path('contacts/', contacts),

]