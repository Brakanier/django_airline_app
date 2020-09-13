from django.shortcuts import render
from rest_framework.generics import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView

from airlines.models import Airline
from airlines.serializers import AirlineSerializer


class AirlineView(APIView):
    def get(self, request):
        airlines = Airline.objects.all()
        serializer = AirlineSerializer(airlines, many=True)
        return Response({"airlines": serializer.data})

    def post(self, request):
        airline = request.data.get('airline')

        serializer = AirlineSerializer(data=airline)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({"success": f"Airline {serializer.instance.pk} created"})

    def put(self, request, pk):
        airline = get_object_or_404(Airline.objects.all(), pk=pk)
        data = request.data.get('airline')
        serializer = AirlineSerializer(instance=airline, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'success': f'Airline {airline.pk} updated'})

    def delete(self, request, pk):
        airline = get_object_or_404(Airline.objects.all(), pk=pk)
        airline.delete()
        return Response({'success': f'Airline {airline.pk} deleted'})
