from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class ShoppingList (models.Model):

    name = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add= True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = ("ShoppingList")
        verbose_name_plural = ("ShoppingLists")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ShoppingList_detail", kwargs={"pk": self.pk})