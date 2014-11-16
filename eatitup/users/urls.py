from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^login/', 'django.contrib.auth.views.login', name="user_login"),
    url(r'^logout/', 'django.contrib.auth.views.logout', name="user_logout")
)