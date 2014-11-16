from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget
from autocomplete_light import ChoiceWidget
from .models import Item

class ItemModelForm(ModelForm):
    class Meta:
        model = Item
        exclude = ['owner']
        widgets = {
            'food': ChoiceWidget(
                'FoodAutocomplete',
                attrs={'placeholder': 'Start Typing'}
            ),
            'unit': ChoiceWidget('UnitAutocomplete',
                attrs={'placeholder': "Start Typing"}
            ),
            'use_by_date': SelectDateWidget(),
        }
