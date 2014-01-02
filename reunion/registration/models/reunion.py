from django.db import models
from .location import Location


class Reunion(models.Model):
    """
    Single occurrance of a reunion.
    """
    start = models.DateTimeField()
    end = models.DateTimeField()
    location = models.ForeignKey(Location, related_name='reunions')
