from django.shortcuts import render
from food.models import Category, Food
from .forms import FoodModelForm

def index(request):
    foods = Food.objects.all().filter(is_approved=True)
    c = {
        'foods': foods,
    }
    return render(request, 'food/index.html', c)

def add(request):

    if request.method == 'POST':
        food_form = FoodModelForm(request.POST)
        if food_form.is_valid():
            food = food_form.save(commit=False)
            food.is_approved = False
            food.save()
            return render(request, 'food/index.html')
    else:
        food_form = FoodModelForm()

    c = {
        'food_form': food_form,
    }

    return render(request, 'food/add.html', c)
