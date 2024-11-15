from django.contrib import admin
from django.db import models

from .models import Dish
from tinymce.widgets import TinyMCE


class DishAdmin(admin.ModelAdmin):
    fields = ['dish_title', 
              'dish_image', 
              'dish_ingredients',
              'dish_cooking_process', 
              'dish_published',
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}

    }

admin.site.register(Dish, DishAdmin)
 