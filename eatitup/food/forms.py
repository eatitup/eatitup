from django.forms import ModelForm
from .models import Food

class FoodModelForm(ModelForm):
    class Meta:
        model = Food
        exclude = ('is_approved', 'notification_period',)
