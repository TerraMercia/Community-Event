from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "location", "event_datetime")
    search_fields = ("title", "location", "description")
    list_filter = ("event_datetime",)

# Register your models here.
