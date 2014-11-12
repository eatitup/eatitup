import autocomplete_light

from food.models import Unit
from .models import Item

autocomplete_light.register(Unit)
autocomplete_light.register(Item)