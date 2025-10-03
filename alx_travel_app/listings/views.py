from rest_framework import viewsets
from .models import TravelListing, Booking
from .serializers import TravelListingSerializer, BookingSerializer

class TravelListingViewSet(viewsets.ModelViewSet):
    """
    Provides CRUD operations for TravelListing
    """
    queryset = TravelListing.objects.all()
    serializer_class = TravelListingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    """
    Provides CRUD operations for Booking
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
