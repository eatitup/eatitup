from django.utils import timezone
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
    use_by_date = models.DateTimeField()

    def __str__(self):
        """ Return the foods name
        """
        return self.food.name

    def is_out_of_date(self):
        """ Is the food item out of date?
        """
        if timezone.now() > self.use_by_date:
            return True
        return False
