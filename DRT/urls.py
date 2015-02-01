__author__ = 'basnal'
from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'DRT.views.showMap'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^map/', 'DRT.views.showMap'),
    url(r'^setpath/$', 'DRT.views.setPath'),
    url(r'^admin/', include(admin.site.urls)),
)
