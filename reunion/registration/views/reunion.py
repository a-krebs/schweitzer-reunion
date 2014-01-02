from rest_framework import generics

from registration.models import Reunion
from registration.serializers import ReunionSerializer


class ReunionList(generics.ListCreateAPIView):
    """
    List all Reunion objects.
    """
    queryset = Reunion.objects.all()
    serializer_class = ReunionSerializer
    
    def __init__(self, *args, **kwargs):
        super(ReunionList, self).__init__(*args, **kwargs)