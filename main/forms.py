from django import forms

from .models import Dish

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ('dish_title','dish_image', 'dish_ingredients', 'dish_cooking_process')
        labels = {
            'dish_title': 'Name of your dish',
            'dish_image': 'Picture of your dish',
            'dish_ingredients': 'Ingredients',
            'dish_cooking_process': 'How to cook?',
        }

class SearchForm(forms.Form):
    search = forms.CharField(label = 'search', max_length= 100)
