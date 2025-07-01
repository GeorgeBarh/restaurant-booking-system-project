# Valid form submission with all required fields
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

# Missing name field should cause validation failure
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

# Missing date field should cause validation failure
def test_missing_date_makes_form_invalid(self):
    form = BookingForm({
        'name': 'John Doe',
        'email': 'john@example.com',
        'phone': '123456789',
        'guests': 2,
        'time': '18:00',
    })
    self.assertFalse(form.is_valid(), msg="Form should be invalid without a date")

# Missing time field should cause validation failure
def test_missing_time_makes_form_invalid(self):
    form = BookingForm({
        'name': 'John Doe',
        'email': 'john@example.com',
        'phone': '123456789',
        'guests': 2,
        'date': (date.today() + timedelta(days=1)).isoformat(),
    })
    self.assertFalse(form.is_valid(), msg="Form should be invalid without a time")

# Form still valid for a past date (validation done in view, not form)
def test_past_booking_is_invalid(self):
    form = BookingForm({
        'name': 'Late Larry',
        'email': 'larry@example.com',
        'phone': '000111222',
        'guests': 2,
        'date': (date.today() - timedelta(days=1)).isoformat(),
        'time': '18:00',
    })
    self.assertTrue(form.is_valid(), msg="Form is valid, but the view will reject past bookings.")
