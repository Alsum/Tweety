from django.conf.urls import include, url

urlpatterns = [
    # Examples:
    # url(r'^$', 'tweety.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'tweetsapp.views.get_tweeets', name="get_tweets"),
]
