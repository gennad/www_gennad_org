from django.conf.urls.defaults import *
from gennadapp.views import archive, twitter_connect

urlpatterns = patterns(
    '',
    url(r'^$', archive),
    url(r'^twitter/connect/$', twitter_connect),
)
