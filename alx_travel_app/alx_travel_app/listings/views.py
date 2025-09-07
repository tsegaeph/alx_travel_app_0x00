from rest_framework import generics
from .models import TravelListing
from .serializers import TravelListingSerializer

# List all travel listings or create a new one
class TravelListingListCreate(generics.ListCreateAPIView):
    queryset = TravelListing.objects.all()
    serializer_class = TravelListingSerializer

# Retrieve, update, or delete a single travel listing
class TravelListingRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = TravelListing.objects.all()
    serializer_class = TravelListingSerializer
