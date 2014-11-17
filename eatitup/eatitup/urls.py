from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', include('users.urls')),
    url(r'^food/', include('food.urls')),
    url(r'^store_cupboard/', include('store_cupboard.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^autocomplete/', include('autocomplete_light.urls'), name="auto_complete"),
)
