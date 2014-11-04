from django.shortcuts import render
from store_cupboard.models import Item

def index(request):
    """ Index of store cupboard
    """
    user = request.user
    items = Item.objects.filter(owner=user)
    print items

    c = {
        'items': items
    }

    return render(request, 'store_cupboard/index.html', c)