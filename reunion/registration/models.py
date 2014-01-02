from django.db import models


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