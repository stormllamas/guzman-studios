from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .serializers import BookingSerializer
from .models import Booking


class BookingAPI(GenericAPIView):
    serializer_class = BookingSerializer

    def get(self, _, pk=None):
        booking = get_object_or_404(Booking, id=pk)

        return Response({
            "id": booking.id,
            "price": booking.price,
            "creation_date": booking.creation_date,
        })
