__author__ = 'basnal'
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^drt/', include('DRT.urls')),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^map/', include('GoogleMapAPI.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
