from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^all/', views.index, name="food_index"),
    url(r'^add/', views.add, name="food_add"),
)