from django.db import models
from django.urls import reverse

class Store (models.Model):

    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("store")
        verbose_name_plural = ("stores")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("store_detail", kwargs={"pk": self.pk})