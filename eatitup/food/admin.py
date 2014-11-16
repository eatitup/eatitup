from django.contrib import admin
from .models import Category, Food, Unit, UnitConversion

admin.site.register(Category)
admin.site.register(Food)
admin.site.register(Unit)
admin.site.register(UnitConversion)
