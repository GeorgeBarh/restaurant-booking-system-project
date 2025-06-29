from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from .models import Booking
from datetime import time
from django.utils import timezone
from django.core.exceptions import ValidationError


class BookingForm(forms.ModelForm):
    guests = forms.IntegerField(
        min_value=1,
        max_value=6,
        label="Number of Guests",
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone', 'guests', 'date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Generate time slots from 12:00 to 22:00 in 30-min increments
        slots = []
        current = time(12, 0)
        while current < time(22, 0):
            slots.append((current.strftime("%H:%M"), current.strftime("%H:%M")))
            hour, minute = current.hour, current.minute + 30
            if minute == 60:
                hour += 1
                minute = 0
            current = time(hour, minute)

        self.fields['time'] = forms.ChoiceField(choices=slots)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('name'),
            Field('email'),
            Field('phone'),
            Field('guests'),
            Field('date'),
            Field('time'),
            Submit('submit', 'Book Table', css_class='btn btn-primary w-100 mt-3')
        )

    def clean_date(self):
        date = self.cleaned_data['date']
        if date < timezone.localdate():
            raise ValidationError("You cannot book for a past date.")
        return date