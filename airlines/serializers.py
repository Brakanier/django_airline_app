from rest_framework import serializers
from airlines.models import Airline

class AirlineSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=32)
    is_vip = serializers.BooleanField()

    def create(self, validated_data):
        return Airline.objects.create(**validated_data)

    def update(self, instance: Airline, validated_data):
        instance.name = validated_data.get('title', instance.name)
        instance.is_vip = validated_data.get('is_vip', instance.is_vip)
        instance.save()
        return instance



