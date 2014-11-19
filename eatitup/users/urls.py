from django.conf.urls import patterns, url
from users import views

urlpatterns = patterns('',
    url(r'^login/', 'django.contrib.auth.views.login', name="user_login"),
    url(r'^logout/', 'django.contrib.auth.views.logout', name="user_logout"),
    url(r'^profile/', views.view, name="user_profile"),
)