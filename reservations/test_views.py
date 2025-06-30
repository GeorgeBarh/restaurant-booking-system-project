from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from reservations.models import Booking, Table
from datetime import date, time


class TestBookingViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="tester", password="testpass123")
        self.table = Table.objects.create(number=1, seats=4)
        self.booking = Booking.objects.create(
            user=self.user,
            name="John Doe",
            email="john@example.com",
            phone="1234567890",
            guests=2,
            date=date.today(),
            time=time(18, 0),
            table=self.table,
            notes="Window seat"
        )

    def test_edit_booking_view_get(self):
        self.client.login(username="tester", password="testpass123")
        response = self.client.get(
            reverse('edit_booking', args=[self.booking.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Edit")

    def test_edit_booking_view_post_valid_data(self):
        self.client.login(username="tester", password="testpass123")
        response = self.client.post(
            reverse('edit_booking', args=[self.booking.pk]),
            {
                'name': 'Jane Doe',
                'email': 'jane@example.com',
                'phone': '9876543210',
                'guests': 2,
                'date': date.today(),
                'time': '18:30',
                'notes': 'New seat',
            },
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Booking updated successfully.")

    def test_cancel_booking_view(self):
        self.client.login(username="tester", password="testpass123")
        response = self.client.post(
            reverse('cancel_booking', args=[self.booking.pk]),
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Your reservation has been canceled.")
