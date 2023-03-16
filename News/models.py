from django.db import models


class News(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/news/')
    about = models.TextField(max_length=2000)
    link = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f"{self.name}"
