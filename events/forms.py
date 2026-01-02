from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["title", "description", "location", "event_datetime"]
        widgets = {
            "event_datetime": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }
