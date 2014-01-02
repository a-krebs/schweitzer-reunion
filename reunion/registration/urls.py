from django.conf.urls import patterns, url

from registration.views import ReunionList, LocationList

urlpatterns = patterns('',
    url(r'^reunions/$', ReunionList.as_view(), name='reunion_list'),
    url(r'^locations/$', LocationList.as_view(), name='location_list'),
#    url(r'^reunions/(?P<pk>[0-9]+)$', ReunionDetail, name='reunion_detail'),
)
