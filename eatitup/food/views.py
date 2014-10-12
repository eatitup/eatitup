from django.shortcuts import render
from food.models import Category, Food

def index(request):
    foods = Food.objects.all()
    c = {
        'foods': foods,
    }
    return render(request, 'food/index.html', c)