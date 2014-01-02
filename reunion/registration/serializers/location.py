from registration.models import Location
from rest_framework import serializers


class LocationSerializer(serializers.ModelSerializer):
    """
    Serialize Location Model.
    """
    def __init__(self, *args, **kwargs):
        super(LocationSerializer, self).__init__(*args, **kwargs)

    class Meta:
        model = Location
