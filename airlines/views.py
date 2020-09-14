from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.permissions import DjangoModelPermissions

from .serializers import AirlineSerializer
from .models import Airline


class AirlineViewSet(ModelViewSet):
    serializer_class = AirlineSerializer
    permission_classes = [DjangoModelPermissions]
    queryset = Airline.objects.all()

