from django.db import models


class Hall(models.Model):
    name = models.CharField(max_length=200)


class Event(models.Model):
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/events/')
    from_date = models.DateField()
    to_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    about = models.TextField(max_length=2000)
    hall_id = models.ForeignKey(Hall, on_delete=models.CASCADE, related_name='events')
    popularity = models.PositiveSmallIntegerField()
