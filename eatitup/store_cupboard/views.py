from django.shortcuts import render

from store_cupboard.models import Item
from store_cupboard.forms import UnitModelForm, ItemModelForm

def index(request):
    """ Index of store cupboard
    """
    user = request.user
    items = Item.objects.filter(owner=user)

    c = {
        'items': items
    }

    return render(request, 'store_cupboard/index.html', c)

def add(request):
    """ Add a new item to the users store cupboard
    """
    user = request.user

    if request.method == 'POST':
        unit_form = UnitModelForm(request.POST)
        item_form = ItemModelForm(request.POST)
    else:
        unit_form = UnitModelForm()
        item_form = ItemModelForm()

    c = {
        'unit_form': unit_form,
        'item_form': item_form,
    }

    return render(request, 'store_cupboard/add.html', c)