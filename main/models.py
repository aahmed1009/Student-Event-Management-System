from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Event(models.Model):
    """Model representing an event or activity"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organized_events')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

    def is_past(self):
        """Check if the event date has passed"""
        return self.date < timezone.now()

    def registered_students_count(self):
        """Get count of registered students"""
        return self.registrations.count()


class Registration(models.Model):
    """Model representing a student's registration for an event"""
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registrations')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'event')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.student.username} - {self.event.title}"
