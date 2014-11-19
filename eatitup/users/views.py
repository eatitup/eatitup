from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def view(request):
    """ User profile
    """
    user = request.user

    c = {
        user: 'user'
    }

    return render(request, 'users/view.html', c)