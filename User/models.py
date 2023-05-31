from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    profile_pic = models.ImageField(upload_to='images/users/', blank=True, default="images/default_user.jpg")

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if self.user:
            self.user.username = self.name
            self.user.save()
        super().save(*args, **kwargs)