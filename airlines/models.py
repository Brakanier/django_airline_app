from django.contrib.auth.models import User
from django.db import models


class Airline(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    is_vip = models.BooleanField(default=False)


class Flight(models.Model):
    id = models.IntegerField(primary_key=True)
    airline = models.ForeignKey(Airline, related_name='flights', on_delete=models.CASCADE)

    seats = models.SmallIntegerField()
    datetime = models.DateTimeField()
    from_city = models.CharField(max_length=32)
    to_city = models.CharField(max_length=32)


