from django.db import models


class Category(models.Model):

    """ Category Model
    """

    name = models.CharField(max_length=50)

    def __str__(self):
        """ Return categories name
        """
        return self.name


class Food(models.Model):

    """ Food Model
    """

    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, blank=True)

    def __str__(self):
        """ Return foods name
        """
        return self.name

class Unit(models.Model):
    """ Unit model
    """

    name = models.CharField(max_length=20)

    def __str__(self):
        """ Return Units name
        """
        return self.name