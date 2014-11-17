from django.utils import timezone
from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from food.models import Food, Unit

class ItemManager(models.Manager):
    """ Custom manager for items
    """

    def get_out_of_date(self, user):
        """ Return all the items which are out of date for a specific user
        """
        return self.get_query_set().filter(self.is_out_of_date()==True)

class Item(models.Model):

    """ Item Model
        Represents a food item inside a users storecupboard
    """

    owner = models.ForeignKey(User)
    food = models.ForeignKey(Food)
    quantity = models.IntegerField(max_length=10)
    unit = models.ForeignKey(Unit)
    use_by_date = models.DateTimeField()

    objects = ItemManager()

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

    def is_nearing_end_of_life(self):
        """ Is the food nearing the end of it's life?
        """
        if timezone.now() + timedelta(days=self.food.notification_period) > self.use_by_date:
            return True
        return False
