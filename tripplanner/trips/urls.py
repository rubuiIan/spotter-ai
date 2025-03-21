from django.urls import path
from . views import (
    TripListCreateView, TripDetailView,
    StopListCreateView, StopDetailView,
    LogEntryListCreateView, LogEntryLDetailCreateView
)

urlpatterns = [
    path('trips/', TripListCreateView.as_view(), name='trip-list-create'),
    path('trips/<int:pk>/', TripDetailView.as_view(), name='trip-detail'),
    
     path('stops/', StopListCreateView.as_view(), name='stop-list-create'),
     path('stops/<int:pk>/', StopDetailView.as_view(), name='stop-list-detail'),
     
     path('log/', LogEntryListCreateView.as_view(), name='log-list-create'),
     path('log/<int:pk>/', LogEntryLDetailCreateView.as_view(), name='stop-list-detail'),
]
