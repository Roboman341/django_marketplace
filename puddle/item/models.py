from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    # after model creation the db needs to be updated
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)  # ordering by name
        verbose_name_plural = "Categories"  # to fix 'Categorys' in django admin view

    # overwrite the string representation for categories name in admin view
    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(
        Category, related_name="items", on_delete=models.CASCADE, default=""
    )  # delete all the items if category deleted
    name = models.CharField(max_length=255)
    # in case user don't want to provide description
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    # django will automatically create the folder for images. will require
    # Pillow python library
    image = models.ImageField(upload_to="item_images", blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        User, related_name="items", on_delete=models.CASCADE
    )  # delete user is all items are deleted
    created_at = models.DateTimeField(
        auto_now_add=True)  # automatically add timestamp

    # overwrite the string representation for categories name in admin view
    def __str__(self):
        return self.name
