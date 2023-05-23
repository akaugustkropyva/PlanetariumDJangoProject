import re

from User.models import Customer
from django import forms
from django.contrib.auth.models import User


class CustomerForm(forms.ModelForm):
    delete_photo = forms.BooleanField(required=False)

    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone'].required = False

    def save(self, commit=True):
        customer = super().save(commit=False)
        if commit:
            customer.save()
            customer.user.username = customer.name
            customer.user.email = customer.email
            customer.user.save()
        return customer

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name and User.objects.filter(username=name).exists():
            if self.instance and self.instance.user.username == name:
                return name
            raise forms.ValidationError("Це ім'я вже використовується!")
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exists():
            if self.instance and self.instance.user.email == email:
                return email
            raise forms.ValidationError('Ця пошта вже використовується')
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone:
            pattern = r'^\+38\d{10}$'
            if not re.match(pattern, phone):
                raise forms.ValidationError("Телефон має бути у форматі +38 ХХХ ХХХХХХХ")
        return phone