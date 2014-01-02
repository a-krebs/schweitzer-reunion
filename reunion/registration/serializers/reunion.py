from registration.models.reunion import Reunion
from rest_framework import serializers


class ReunionSerializer(serializers.ModelSerializer):
    """
    Serialize Reunion Model.
    """
    def __init__(self, *args, **kwargs):
        super(ReunionSerializer, self).__init__(*args, **kwargs)
    
    class Meta:
        model = Reunion