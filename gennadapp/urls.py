from django.conf.urls.defaults import *

from django.contrib import admin
from gennadapp.views import archive

urlpatterns = patterns(
    '',
    url(r'^$', archive),
    url(r'^twitter/connect/$', twitter_connect),
)
