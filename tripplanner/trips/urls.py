from django.urls import path
from .views import (
    home, TripListCreateView, TripDetailView, 
    StopListCreateView, StopDetailView, 
    LogEntryListCreateView, LogEntryDetailView
)

urlpatterns = [
    path('', home, name='home'),
    path('trips/', TripListCreateView.as_view(), name='trip-list'),
    path('trips/<int:pk>/', TripDetailView.as_view(), name='trip-detail'),
    path('stops/', StopListCreateView.as_view(), name='stop-list'),
    path('stops/<int:pk>/', StopDetailView.as_view(), name='stop-detail'),
    path('logs/', LogEntryListCreateView.as_view(), name='logentry-list'),
    path('logs/<int:pk>/', LogEntryDetailView.as_view(), name='logentry-detail'),
]