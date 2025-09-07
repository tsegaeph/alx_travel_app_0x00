from django.urls import path
from . import views

urlpatterns = [
    path('travel-listings/', views.TravelListingListCreate.as_view(), name='travellisting-list-create'),
    path('travel-listings/<int:pk>/', views.TravelListingRetrieveUpdateDelete.as_view(), name='travellisting-rud'),
]
