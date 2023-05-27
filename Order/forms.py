import re
from django.core.validators import validate_email
from django import forms
from .models import Customer
from django.forms import DateInput
from django.contrib.auth.models import User


class OrderForm(forms.ModelForm):
    card_number = forms.CharField(max_length=16, required=True)
    card_date = forms.DateField(widget=DateInput(attrs={'type': 'date'}), required=True)
    card_cvv = forms.CharField(max_length=3, required=True)

    class Meta:
        model = Customer
        fields = ['name', 'phone', 'email', 'card_number', 'card_date', 'card_cvv']

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        if self.instance.user:
            self.fields['name'].disabled = True
            self.fields['phone'].disabled = True
            self.fields['email'].disabled = True
        self.fields['phone'].required = False

    def clean_card_number(self):
        card_number = self.cleaned_data['card_number']
        if len(card_number) != 16:
            raise forms.ValidationError('Номер карти має бути 16 цифр')
        return card_number

    def clean_card_cvv(self):
        card_cvv = self.cleaned_data['card_cvv']
        if len(card_cvv) != 3:
            raise forms.ValidationError('Код CVV має бути 3 цифри')
        return card_cvv

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not self.instance.user and User.objects.filter(username=name).exists():
            raise forms.ValidationError("Це ім'я вже використовується!")
        return name

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            validate_email(email)
        except forms.ValidationError:
            raise forms.ValidationError('Некоректний email')

        if not self.instance.user and User.objects.filter(email=email).exists():
            raise forms.ValidationError('Цей email вже використовується')

        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone:
            pattern = r'^\+38\d{10}$'
            if not re.match(pattern, phone):
                raise forms.ValidationError("Телефон має бути у форматі +38 ХХХ ХХХХХХХ")
        return phone

    def user_is_registered(self):
        return self.initial.get('user') is not None
