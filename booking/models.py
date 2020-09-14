from django.contrib.auth.models import User
from django.db import models

from airlines.models import Flight


# Create your models here.
class BookFlights(models.Model):
    id = models.IntegerField(primary_key=True)
    flight = models.ForeignKey(Flight, related_name='book_flights', on_delete=models.CASCADE)
    client = models.ForeignKey(User, related_name='book_flights', on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
