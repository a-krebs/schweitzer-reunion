from rest_framework import generics

from registration.models import Location
from registration.serializers import LocationSerializer


class LocationList(generics.ListCreateAPIView):
    """
    List all Location objects.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def __init__(self, *args, **kwargs):
        super(LocationList, self).__init__(*args, **kwargs)
