from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/events/')
    from_date = models.DateField()
    to_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    about = model.TextField(max_length=2000)
    hall_id = models.ForeignKey(Hall, on_delete=models.CASCADE, related_name='events')
    popularity = models.PositiveSmallIntegerField()


class Hall(models.Model):
    name = models.CharField(max_length=200)


class News(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/news/')
    about = model.TextField(max_length=2000)
    link = models.TextField(max_length=500, blank=True)


class Info(models.Model):
    text = model.TextField(max_length=2000)
    hall_id = models.ForeignKey(Hall, on_delete=models.CASCADE, related_name='events')


class Proposal(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/proposals/')
