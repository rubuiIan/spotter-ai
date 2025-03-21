from rest_framework import generics, permissions
from .models import Trip, Stop, LogEntry
from .serializers import TripSerializer, StopSerializer, LogEntrySerializer

# Trip views
class TripListCreateView(generics.ListCreateAPIView):
    queryset = Trip.objects.all()
    selializers_class = TripSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
# Trip details
class TripDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trip.objects.all()
    serializer_class =TripSerializer
    permission_classes = [permissions.IsAuthenticated]
    
# Stop view
class StopListCreateView(generics.ListCreateAPIView):
    queryset = Stop.objects.all()
    serializer_class = StopSerializer
    permission_classes = [permissions.IsAuthenticated]

class StopDetailView(generics.RetrieveDestroyAPIView):
    queryset = Stop.objects.all()
    serializer_class = StopSerializer
    permission_classes = [permissions.IsAuthenticated]
    
# Log entry
class LogEntryListCreateView(generics.ListCreateAPIView):
    queryset = LogEntry.objects.all()
    serializer_class = StopSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class LogEntryLDetailCreateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LogEntry.objects.all()
    serializer_class = StopSerializer
    permission_classes = [permissions.IsAuthenticated]
