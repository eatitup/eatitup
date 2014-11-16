from django.forms import ModelForm
import autocomplete_light
from .models import Item

class ItemModelForm(ModelForm):
    class Meta:
        model = Item
        exclude = ['owner']
        widgets = {
            'food': autocomplete_light.ChoiceWidget(
                'FoodAutocomplete',
                attrs={'placeholder': 'Start Typing'}),
            'unit': autocomplete_light.ChoiceWidget('UnitAutocomplete')
        }
