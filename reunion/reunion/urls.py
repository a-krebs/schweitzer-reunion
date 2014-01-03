from django.conf.urls import patterns, include, url, static
from django.contrib import admin

from registration import urls as registration_urls
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(registration_urls, namespace='registration'))
) + static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
