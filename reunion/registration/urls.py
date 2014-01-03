from django.conf.urls import patterns, url, include

from registration.views import ReunionList, LocationList, RegistrationList
from registration.views import BaseApplicationView

api_urls = patterns('',
    url(r'^reunions/$', ReunionList.as_view(), name='reunion_list'),
    url(r'^locations/$', LocationList.as_view(), name='location_list'),
    url(r'^registrations/$', RegistrationList.as_view(), name='registration_list'),
#    url(r'^reunions/(?P<pk>[0-9]+)$', ReunionDetail, name='reunion_detail'),
)

application_urls = patterns('',
    url(r'^$', BaseApplicationView.as_view(), name='main'),
)

urlpatterns = patterns('',
    url(r'^api/', include(api_urls, namespace='api')),
    url(r'', include(application_urls, namespace='application')),
)