from django.conf.urls.defaults import *

handler500 = 'djangotoolbox.errorviews.server_error'

from django.contrib import admin
from gennadapp.views import python, django, algorithms, twisted, gevent
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', include('gennadapp.urls')),
    #(r'^twitter/connect/$', include('gennadapp.urls')),
    (r'^twitter/connect/$', 'gennadapp.views.twitter_connect'),

    (r'^python/$', python),
    (r'^django/$', django),
    (r'^algorithms/$', algorithms),
    (r'^twisted/$', twisted),
    (r'^gevent/$', gevent),

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    ('^$', 'django.views.generic.simple.direct_to_template', {'template': 'home.html'}),
    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

)
