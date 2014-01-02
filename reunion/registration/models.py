from django.db import models
from django.contrib.auth.models import User

from reunion.settings import CHARFIELD_MAX_LEN


class Location(models.Model):
    """
    Geographical location.
    """
    name = models.TextField(blank=True)


class Reunion(models.Model):
    """
    Single occurrance of a reunion.
    """
    start = models.DateTimeField()
    end = models.DateTimeField()
    location = models.ForeignKey(Location, related_name='reunions')


class Registration(models.Model):
    """
    A physical person that will be attending a reunion.
    """
    first_name = models.CharField(max_length=CHARFIELD_MAX_LEN)
    last_name = models.CharField(max_length=CHARFIELD_MAX_LEN)
    start = models.DateTimeField()
    end = models.DateTimeField()
    regstered_by = models.ForeignKey(User, related_name='registrations')
    reunion = models.ForeignKey(Reunion, related_name='registrations')
