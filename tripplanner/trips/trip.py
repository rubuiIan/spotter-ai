from rest_framework import serializers
from .models import Trip, Stop, LogEntry
from django.contrib.auth import get_user_model

User = get_user_model()

# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_driver']
        
# Stop serializer
class StopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stop
        fields = '__all__'
        
# Log entry
class LogEntrySerializer(serializers.ModelSerializer):
    class Meta:
        models = LogEntry
        fields = '__all__'
        
# Trip serializer
class TripSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    stops = StopSerializer(many=True, read_only=True)
    logs = LogEntrySerializer(many=True, read_only=True)
    
    class Meta:
        model = Trip
        fields = '__all__'