from django.conf.urls import patterns, include, url
from django.contrib import admin

from registration import urls as registration_urls

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^registration/api/', include(registration_urls, namespace='registration'))
)
