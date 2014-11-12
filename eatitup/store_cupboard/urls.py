from django.conf.urls import patterns, url
from store_cupboard import views

urlpatterns = patterns('',
    url(r'^index/', views.index, name="store_cupboard_index"),
    url(r'^add/', views.add, name="store_cupboard_add")
)