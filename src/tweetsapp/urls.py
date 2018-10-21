from django.conf.urls import include, url
from . import views
urlpatterns = [
    # Examples:
    url(r'^$', views.login_twitter, name="login_twitter"),
    url(r'^callback/$', views.callback, name="callback"),
    url(r'^get-tweets/$', views.get_tweeets, name="get_tweets"),
]
