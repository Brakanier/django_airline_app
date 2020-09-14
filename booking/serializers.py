from rest_framework import serializers
from .models import FlightBooking


class FlightBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightBooking
        fields = ('flight__airline__name', 'flight__from_city', 'flight__to_city', 'flight__datetime')
