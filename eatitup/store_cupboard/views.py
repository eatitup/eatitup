from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from store_cupboard.models import Item
from store_cupboard.forms import ItemModelForm

@login_required
def index(request):
    """ Index of store cupboard
    """
    user = request.user
    # items = Item.objects.filter(owner=user)

    items = Item.objects.filter(owner=user)

    c = {
        'items': items
    }

    return render(request, 'store_cupboard/index.html', c)

@login_required
def add(request):
    """ Add a new item to the users store cupboard
    """
    user = request.user

    if request.method == 'POST':
        item_form = ItemModelForm(request.POST)
        item = item_form.save(commit=False)
        item.owner = user
        item.save()

        return redirect('store_cupboard_index')

    else:
        item_form = ItemModelForm()

    c = {
        'item_form': item_form,
    }

    return render(request, 'store_cupboard/add.html', c)