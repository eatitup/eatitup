from django.utils import timezone
from django.db import models


class Category(models.Model):

    """ Category Model
    """

    name = models.CharField(max_length=50)

    def __str__(self):
        """ Return categories name
        """
        return self.name


class Unit(models.Model):

    """ Unit model
    """

    name = models.CharField(max_length=20)
    short_name = models.CharField(max_length=5)

    def __str__(self):
        """ Return Units name
        """
        return self.name


class UnitConversion(models.Model):

    """ Converts between different units
    """

    unit_a = models.ForeignKey(Unit, related_name="unit a")
    unit_b = models.ForeignKey(Unit, related_name="unit b")
    conversion = models.FloatField()

    def __str__(self):
        """ Return Conversion name
        """
        return "%s - %s" % (self.unit_a, self.unit_b)

    def convert_a_to_b(self):
        """ Converts unit a to unit b
        """
        return unit_a * conversion

    def convert_b_to_a(self):
        """ Converts unit b to unit a
        """
        return unit_b / conversion


class Food(models.Model):

    """ Food Model
    """

    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, blank=True)
    default_unit = models.ForeignKey(Unit, blank=True)
    notification_period = models.IntegerField(default=7)
    is_approved = models.BooleanField(default=None)

    def __str__(self):
        """ Return foods name
        """
        return self.name
