from django.db import models


class Category(models.Model):

    """ Category Model
    """

    name = models.CharField(max_length=50)

    def __str__(self):
        """ Override for __str__ method
        """
        return self.name


class Food(models.Model):

    """ Food Model
    """

    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, blank=True)

    def __str__(self):
        """ Override for __str__ method
        """
        return self.name
