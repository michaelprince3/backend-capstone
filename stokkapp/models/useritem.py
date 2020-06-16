from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from .item import Item
from .location import Location
from .category import Category
from .store import Store


class UserItem (models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    size = models.CharField(max_length=50)
    quantity = models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    expiration = models.DateTimeField(auto_now_add= False)
    purchase_date = models.DateTimeField(auto_now_add= True)

    class Meta:
        verbose_name = ("item")
        verbose_name_plural = ("items")

    def __str__(self):
        return Item.name

    def get_absolute_url(self):
        return reverse("item_detail", kwargs={"pk": self.pk})