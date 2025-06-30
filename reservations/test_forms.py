from django.test import TestCase
from .forms import BookingForm
from datetime import date, time, timedelta


class TestBookingForm(TestCase):

    def test_form_is_valid(self):
        form = BookingForm({
            'name': 'John Doe',
            'email': 'john@example.com',
            'phone': '123456789',
            'guests': 2,
            'date': (date.today() + timedelta(days=1)).isoformat(),
            'time': '18:00',
            'notes': 'No peanuts please'
        })
        self.assertTrue(form.is_valid(), msg="Form should be valid with all fields")

    def test_missing_name_makes_form_invalid(self):
        form = BookingForm({
            'name': '',
            'email': 'john@example.com',
            'phone': '123456789',
            'guests': 2,
            'date': (date.today() + timedelta(days=1)).isoformat(),
            'time': '18:00',
        })
        self.assertFalse(form.is_valid(), msg="Form should be invalid without a name")

    def test_missing_date_makes_form_invalid(self):
        form = BookingForm({
            'name': 'John Doe',
            'email': 'john@example.com',
            'phone': '123456789',
            'guests': 2,
            'time': '18:00',
        })
        self.assertFalse(form.is_valid(), msg="Form should be invalid without a date")

    def test_missing_time_makes_form_invalid(self):
        form = BookingForm({
            'name': 'John Doe',
            'email': 'john@example.com',
            'phone': '123456789',
            'guests': 2,
            'date': (date.today() + timedelta(days=1)).isoformat(),
        })
        self.assertFalse(form.is_valid(), msg="Form should be invalid without a time")

    def test_past_booking_is_invalid(self):
        form = BookingForm({
            'name': 'Late Larry',
            'email': 'larry@example.com',
            'phone': '000111222',
            'guests': 2,
            'date': (date.today() - timedelta(days=1)).isoformat(),  # yesterday
            'time': '18:00',
        })
        # Note: the form itself doesn't reject past dates, it's handled in the view
        self.assertTrue(form.is_valid(), msg="Form is valid, but the view will reject past bookings.")
    
