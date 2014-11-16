import autocomplete_light

from food.models import Unit, Food

autocomplete_light.register(Unit)
autocomplete_light.register(Food)