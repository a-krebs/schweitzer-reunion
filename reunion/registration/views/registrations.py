from rest_framework import generics

from registration.models import Registration
from registration.serializers import ReunionSerializer


class RegistrationList(generics.ListCreateAPIView):
    """
    List all Reunion objects.
    """
    queryset = Registration.objects.all()
    serializer_class = ReunionSerializer

    def __init__(self, *args, **kwargs):
        super(RegistrationList, self).__init__(*args, **kwargs)
