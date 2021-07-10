from django.db import models
from django.contrib.auth.models import User

class Color(models.Model):
    name = models.CharField(max_length=30, unique=True)

class Coord(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits = 14, decimal_places = 12)
    lng = models.DecimalField(max_digits = 15, decimal_places = 12)
    color = models.ForeignKey(Color, related_name='coord', on_delete=models.CASCADE)
