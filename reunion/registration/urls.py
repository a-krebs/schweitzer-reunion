from django.conf.urls import patterns, url

from registration.views import ReunionList, LocationList, RegistrationList

urlpatterns = patterns('',
    url(r'^reunions/$', ReunionList.as_view(), name='reunion_list'),
    url(r'^locations/$', LocationList.as_view(), name='location_list'),
    url(r'^registrations/$', RegistrationList.as_view(), name='registration_list'),
#    url(r'^reunions/(?P<pk>[0-9]+)$', ReunionDetail, name='reunion_detail'),
)
