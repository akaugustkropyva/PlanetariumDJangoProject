from django.db import models

from django.contrib.auth.models import User


class Hall(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"


class Event(models.Model):
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/events/', default="images/default.png", blank=True)
    from_date = models.DateField()
    to_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    about = models.TextField(max_length=2000)
    hall_id = models.ForeignKey(Hall, on_delete=models.CASCADE, related_name='events')
    popularity = models.PositiveSmallIntegerField()
    favourite = models.ManyToManyField(User, related_name='favourite', blank=True)

    def __str__(self):
        return f"{self.name}"


