from django.db import models
from django.contrib.auth.models import User
from food.models import Food, Unit

class Item(models.Model):

    """ Item Model
        Represents a food item inside a users storecupboard
    """

    owner = models.ForeignKey(User)
    food = models.ForeignKey(Food)
    quantity = models.IntegerField(max_length=10)
    unit = models.ForeignKey(Unit)

    def __str__(self):
        """ Return the foods name
        """
        return self.food.name