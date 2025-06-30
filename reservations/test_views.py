from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from reservations.models import Booking, Table
from django.utils import timezone
from datetime import timedelta, time

class TestMyBookingsView(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.table = Table.objects.create(number=1, seats=4)
        self.booking = Booking.objects.create(
            user=self.user,
            name="John Doe",
            email="john@example.com",
            phone="1234567890",
            guests=2,
            date=timezone.now().date() + timedelta(days=1),
            time=time(18, 0),
            table=self.table,
        )

    def test_my_bookings_view_loads_for_logged_in_user(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(reverse('my_bookings'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "My Bookings")
        self.assertContains(response, "testuser")

    def test_my_bookings_view_redirects_if_not_logged_in(self):
        response = self.client.get(reverse('my_bookings'))
        self.assertRedirects(response, f'/accounts/login/?next={reverse("my_bookings")}')
