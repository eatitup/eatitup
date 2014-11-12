from django.forms import ModelForm
import autocomplete_light
from food.models import Unit
from .models import Item

class UnitModelForm(ModelForm):
    class Meta:
        model = Unit
        # add for django 1.6:
        fields = ['name']
        widgets = {
            'name': autocomplete_light.TextWidget('UnitAutocomplete')
        }

class ItemModelForm(ModelForm):
    class Meta:
        model = Item
        # add for django 1.6:
        fields = ['food']
        widgets = {
            'food': autocomplete_light.TextWidget('ItemAutocomplete')
        }
