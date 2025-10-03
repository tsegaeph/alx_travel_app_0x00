from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TravelListingViewSet, BookingViewSet

router = DefaultRouter()
router.register(r'travel-listings', TravelListingViewSet, basename='travellisting')
router.register(r'bookings', BookingViewSet, basename='booking')

urlpatterns = [
    path('api/', include(router.urls)),  # all CRUD endpoints under /api/
]
