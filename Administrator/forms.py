from Events.models import Event
from django import forms


class EventForm(forms.ModelForm):
    image = forms.ImageField(required=True)

    class Meta:
        model = Event
        fields = '__all__'

    def save(self, commit=True):
        event = super().save(commit=False)
        if commit:
            event.save()
        return event

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price:
            if price < 0.0:
                raise forms.ValidationError("Ціна не може бути від'ємною!")
        elif price == 0.0:
            raise forms.ValidationError("Не може бути безкоштовного квитка!")
        return price

    def clean_popularity(self):
        popularity = self.cleaned_data.get('popularity')
        if popularity < 1 or popularity > 12:
            raise forms.ValidationError("Популярність повинна мати значення у інтервалі від 1 до 12!")
        return popularity
