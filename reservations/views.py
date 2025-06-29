from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.timezone import now
from datetime import datetime
from .models import Booking, Table
from .forms import BookingForm
from django.utils import timezone


class BookTableView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = "reservations/book_table.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        guests = form.cleaned_data['guests']
        date_ = form.cleaned_data['date']
        time_ = form.cleaned_data['time']

        #  Prevent past bookings
        if isinstance(time_, str):
            time_ = datetime.strptime(time_, "%H:%M").time()

        selected_datetime = datetime.combine(date_, time_)
        selected_datetime = timezone.make_aware(selected_datetime)
        if selected_datetime < timezone.now():
            messages.error(self.request, "You cannot book for a past time.")
            return redirect('book_table')

        #  Find available table
        booked_table_ids = Booking.objects.filter(date=date_, time=time_).values_list('table_id', flat=True)
        available_tables = Table.objects.filter(seats__gte=guests).exclude(id__in=booked_table_ids).order_by('seats')

        if available_tables.exists():
            form.instance.table = available_tables.first()
            messages.success(self.request, f"Table reserved for {guests} guests on {date_} at {time_}.")
            return super().form_valid(form)
        else:
            messages.error(self.request, "No tables available for that time and group size.")
            return redirect('book_table')

    def get_success_url(self):
        return "/reservations/my-bookings/"

class MyBookingsView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = "reservations/my_bookings.html"
    context_object_name = "bookings"

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user).order_by("date", "time")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["today"] = timezone.now().date()
        return context