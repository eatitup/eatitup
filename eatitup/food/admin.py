from django.contrib import admin
from .models import Category, Food, Unit, UnitConversion

class FoodAdmin(admin.ModelAdmin):
    """ Customised ModelAdmin for the Food Model
    """

    list_display = ('name', 'category', 'default_unit', 'is_approved',)
    list_filter = ('is_approved',)

admin.site.register(Category)
admin.site.register(Food, FoodAdmin)
admin.site.register(Unit)
admin.site.register(UnitConversion)
