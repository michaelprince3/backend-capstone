from django.db import models
from django.urls import reverse


class Item (models.Model):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    image = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("item")
        verbose_name_plural = ("items")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("item_detail", kwargs={"pk": self.pk})