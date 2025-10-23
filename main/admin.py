from django.contrib import admin
from .models import Event, Registration


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'organizer', 'created_at')
    list_filter = ('date', 'organizer')
    search_fields = ('title', 'description', 'location')
    date_hierarchy = 'date'


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('student', 'event', 'created_at')
    list_filter = ('event', 'created_at')
    search_fields = ('student__username', 'event__title')
    date_hierarchy = 'created_at'
