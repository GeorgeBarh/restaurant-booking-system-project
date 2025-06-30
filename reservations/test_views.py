from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from reservations.models import Booking, Table
from datetime import date, time
from django.utils import timezone
from datetime import timedelta


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

    def test_user_cannot_edit_another_users_booking(self):
        """Ensure users can't access/edit others' bookings"""
        other_user = User.objects.create_user(username="hacker", password="hackpass123")
        self.client.login(username="hacker", password="hackpass123")

        response = self.client.get(reverse('edit_booking', args=[self.booking.pk]))
        self.assertEqual(response.status_code, 404)

    def test_user_cannot_cancel_another_users_booking(self):
        """Ensure users can't cancel others' bookings"""
        other_user = User.objects.create_user(username="hacker", password="hackpass123")
        self.client.login(username="hacker", password="hackpass123")

        response = self.client.post(reverse('cancel_booking', args=[self.booking.pk]), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Booking not found or unauthorized.")

    def test_authenticated_user_can_cancel_own_booking(self):
        self.client.login(username='tester', password='testpass123')
        response = self.client.post(reverse('cancel_booking', args=[self.booking.pk]), follow=True)
        self.assertRedirects(response, reverse('my_bookings'))
        self.assertContains(response, 'Your reservation has been canceled.')
        self.assertFalse(Booking.objects.filter(pk=self.booking.pk).exists())

    def test_unauthenticated_user_cannot_access_edit_booking(self):
        """Unauthenticated users should be redirected to login when accessing edit view"""
        response = self.client.get(reverse('edit_booking', args=[self.booking.pk]), follow=True)
        self.assertRedirects(
            response,
            f"/accounts/login/?next=/reservations/edit/{self.booking.pk}/"
        )

    def test_unauthenticated_user_cannot_cancel_booking(self):
        """Unauthenticated users should be redirected to login when trying to cancel a booking"""
        response = self.client.post(reverse('cancel_booking', args=[self.booking.pk]), follow=True)
        self.assertRedirects(
            response,
            f"/accounts/login/?next=/reservations/cancel/{self.booking.pk}/"
        )

    def test_my_bookings_view_shows_user_bookings(self):
        """Authenticated users should see their own bookings listed"""
        self.client.login(username="tester", password="testpass123")
        response = self.client.get(reverse('my_bookings'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "tester")
        self.assertContains(response, "Window seat")


    def test_my_bookings_view_marks_past_bookings(self):
        """Ensure past bookings are distinguishable in the template context"""
            # Create a past booking
        past_booking = Booking.objects.create(
            user=self.user,
            name="Old Booking",
            email="old@example.com",
            phone="1112223333",
            guests=2,
            date=date.today() - timedelta(days=2),
            time=time(18, 0),
            table=self.table
        )

        self.client.login(username="tester", password="testpass123")
        response = self.client.get(reverse('my_bookings'))

        self.assertEqual(response.status_code, 200)
        self.assertIn(past_booking, response.context['bookings'])
        self.assertIn("today", response.context)
        self.assertLess(past_booking.date, response.context["today"])

    def test_my_bookings_view_shows_only_users_own_bookings(self):
        """Ensure users see only their own bookings in my_bookings view"""
        other_user = User.objects.create_user(username="outsider", password="outpass123")
        other_booking = Booking.objects.create(
            user=other_user,
            name="Intruder",
            email="intruder@example.com",
            phone="9998887777",
            guests=2,
            date=date.today(),
            time=time(20, 0),
            table=self.table
        )

        self.client.login(username="tester", password="testpass123")
        response = self.client.get(reverse('my_bookings'))

        self.assertEqual(response.status_code, 200)
        self.assertIn(self.booking, response.context["bookings"])
        self.assertNotIn(other_booking, response.context["bookings"])

        from django.utils.timezone import now, timedelta

    def test_booking_cannot_be_created_in_past(self):
        """Ensure user cannot book a table in the past"""
        self.client.login(username="tester", password="testpass123")

        past_date = date.today() - timedelta(days=1)
        response = self.client.post(
            reverse("book_table"),
            {
                "name": "John TimeTraveler",
                "email": "future@back.com",
                "phone": "1112223333",
                "guests": 2,
                "date": past_date,
                "time": "18:00",
                "notes": "Trying to book in the past"
            },
            follow=True
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "You cannot book in the past.")



   
