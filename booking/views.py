from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions

from .serializers import FlightBookingSerializer
from .models import FlightBooking


class ClientBookingViewSet(ModelViewSet):
    serializer_class = FlightBookingSerializer
    permission_classes = [DjangoModelPermissions]

    def get_queryset(self):
        return FlightBooking.objects.filter(client=self.request.user)

