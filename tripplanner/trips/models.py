from django.db import models
from django.contrib.auth.models import AbstractUser

# Customer User model 
class CustomerUser(AbstractUser):
    class Meta:
        verbose_name = "Customer User"
        verbose_name_plural = "Customer Users"

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customer_users", 
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customeruser_permissions",
        blank=True,
    )

    def __str__(self):
        return self.username


# Trip model
class Trip(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
    ]

    user = models.ForeignKey(
        CustomerUser, on_delete=models.CASCADE, related_name="trips"
    )
    current_location = models.CharField(max_length=255)
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    current_cycle_hours = models.PositiveIntegerField()
    distance = models.FloatField(null=True, blank=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="pending"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Trip {self.id}: {self.pickup_location} → {self.dropoff_location}"


# Stop model
class Stop(models.Model):
    STOP_TYPE_CHOICES = [
        ("fuel", "Fuel Stop"),
        ("rest", "Rest Stop"),
        ("checkpoint", "Checkpoint"),
    ]

    trip = models.ForeignKey(
        Trip, on_delete=models.CASCADE, related_name="trip_stops"
    )
    location = models.CharField(max_length=255)
    stop_type = models.CharField(max_length=50, choices=STOP_TYPE_CHOICES)
    duration_minutes = models.PositiveIntegerField(default=30)
    scheduled_at = models.DateTimeField()

    def __str__(self):
        return f"Stop at {self.location} ({self.stop_type})"


# Log Entry model
class LogEntry(models.Model):
    STATUS_CHOICES = [
        ("driving", "Driving"),
        ("on_duty", "On Duty"),
        ("off_duty", "Off Duty"),
        ("sleeping", "Sleeping"),
    ]

    trip = models.ForeignKey(
        Trip, on_delete=models.CASCADE, related_name="trip_logs"
    )
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Log {self.id} - {self.trip}: {self.status} ({self.start_time} → {self.end_time})"
