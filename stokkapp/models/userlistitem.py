from django.db import models
from django.urls import reverse
from .item import Item
from .shoppinglist import ShoppingList


class UserListItem (models.Model):

    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    shopping_list = models.ForeignKey(ShoppingList, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = ("UserListItem")
        verbose_name_plural = ("UserListItems")

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse("UserListItem_detail", kwargs={"pk": self.pk})