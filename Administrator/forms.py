from Events.models import Event
from django import forms


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

    def save(self, commit=True):
        event = super().save(commit=False)
        if commit:
            event.save()
        return event
