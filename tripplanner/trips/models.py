from django.db import models
from django.contrib.auth.models import AbstractUser


# Customer use model
class CustomerUser(AbstractUser):
    is_driver = models.BooleanField(default=True)
    
# Trip model
class Trip(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
        
    ]
    
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE, related_name="trips")
    current_location = models.CharField( max_length=255)
    pickup_location = models.CharField( max_length=255)
    dropoff_location = models.CharField( max_length=255)
    current_cycle_hours = models.IntegerField()
    distance = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Trip {self.id} - {self.pickup_location} to {self.dropoff_location}"
    
# Stop Models
class Stop(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name="stops")
    location = models.CharField(max_length=255)
    stop_type = models.CharField( max_length=50, choices=[
        ('fuel', 'Fuel Stop'),
        ('rest', 'Rest Stop'),
        ('checkpoint', 'Checkpoint')
    ])
    duration_minutes = models.IntegerField(default=30)
    scheduled_at = models.DateTimeField()
    
    def __str__(self):
        return f"stop at {self.location} ({self.stop_type})"
    
# Log entry
class LogEntry(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name="stops")
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(max_length=20, choices=[
        ('driving', 'Driving'),
        ('on_duty', 'On Duty'),
        ('off_duty', 'Off Duty'),
        ('sleeping', 'Sleeping')
    ])
    notes = models.TextField(balnk=True)
    
    def __str__(self):
        return f"Log for Trip {self.trip.id} - {self.status} from {self.start_time} to {self.end_time}"