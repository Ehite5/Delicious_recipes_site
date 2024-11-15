from django.db import models
from django.core.validators import FileExtensionValidator
from datetime import datetime

from myssite import settings

class Dish(models.Model):
    dish_title = models.CharField(max_length = 35)
    dish_ingredients = models.TextField()
    dish_cooking_process = models.TextField()
    dish_image = models.ImageField(validators=[FileExtensionValidator(allowed_extensions=settings.ALLOWED_FORMAT_IMAGE)])
    dish_published = models.DateField('date published', default = datetime.now())
    
    def __str__(self):
        return self.dish_title
