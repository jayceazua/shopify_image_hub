from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    caption = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    artist = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def summary(self):
        return self.caption[:100]
