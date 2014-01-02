from django.db import models


class Location(models.Model):
    """
    Geographical location.
    """
    name = models.TextField(blank=True)
