from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from .models import Booking
from datetime import time
from django.core.exceptions import ValidationError

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone', 'guests', 'date', 'time', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.Select(choices=[
                (f"{h:02d}:{m:02d}", f"{h:02d}:{m:02d}")
                for h in range(12, 22)
                for m in (0, 30)
            ])
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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
