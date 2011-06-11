from django.conf.urls.defaults import *
from gennadapp.views import archive

urlpatterns = patterns(
    '',
    url(r'^$', archive),
)
