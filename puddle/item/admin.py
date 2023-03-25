from django.contrib import admin

# to tell django show database model in admin interface

from .models import Category
from .models import Item

admin.site.register(Category)
admin.site.register(Item)
