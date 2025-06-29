from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from .models import Booking

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

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('name'),
            Field('email'),
            Field('phone'),
            Field('guests'),
            Field('date'),
            Field('time'),
            Field('table'),
            Submit('submit', 'Book Table', css_class='btn btn-primary w-100 mt-3')
        )
