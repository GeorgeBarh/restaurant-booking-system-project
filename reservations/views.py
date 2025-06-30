from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.timezone import now
from datetime import datetime,time
from .models import Booking, Table
from .forms import BookingForm
from django.utils import timezone
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.utils.timezone import make_aware
from datetime import datetime

class BookTableView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = "reservations/book_table.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        guests = form.cleaned_data['guests']
        date_ = form.cleaned_data['date']
        time_ = form.cleaned_data['time']

        # Prevent booking in the past
        dt_combined = make_aware(datetime.combine(date_, time_))
        if dt_combined < datetime.now().astimezone():
            messages.error(self.request, " You cannot book in the past.")
            return redirect('book_table')

        # Find available table
        booked_table_ids = Booking.objects.filter(date=date_, time=time_).values_list('table_id', flat=True)
        available_tables = Table.objects.filter(seats__gte=guests).exclude(id__in=booked_table_ids).order_by('seats')

        if available_tables.exists():
            form.instance.table = available_tables.first()
            messages.success(
                self.request,
                f"Table reserved for {guests} guests on {date_} at {time_}."
            )
            return super().form_valid(form)
        else:
            messages.error(self.request, "No tables available for that time and group size.")
            return redirect('book_table')

    def get_success_url(self):
        return reverse_lazy("my_bookings")


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
    
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

@login_required

@login_required
def cancel_booking(request, pk):
    booking = Booking.objects.filter(id=pk, user=request.user).first()
    if booking:
        booking.delete()
        messages.success(request, "Your reservation has been canceled.")
    else:
        messages.error(request, "Booking not found or unauthorized.")
    return redirect("my_bookings")


class UpdateBookingView(LoginRequiredMixin, UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = "reservations/update_booking.html"

    def get_queryset(self):
        # Make sure users can only edit their own bookings
        return Booking.objects.filter(user=self.request.user)

    def form_valid(self, form):
        form.instance.user = self.request.user
        guests = form.cleaned_data['guests']
        date_ = form.cleaned_data['date']
        time_ = form.cleaned_data['time']

        # Prevent editing to a past datetime
        if isinstance(time_, str):
            time_ = datetime.strptime(time_, "%H:%M").time()
        combined = make_aware(datetime.combine(date_, time_))
        if combined < timezone.now():
            messages.error(self.request, " Cannot book in the past.")
            return redirect("my_bookings")

        # Check table availability excluding this booking
        booked_tables = Booking.objects.filter(
            date=date_, time=time_
        ).exclude(id=self.object.id).values_list("table_id", flat=True)

        available_tables = Table.objects.filter(seats__gte=guests).exclude(id__in=booked_tables).order_by("seats")

        if available_tables.exists():
            form.instance.table = available_tables.first()
            messages.success(self.request, " Booking updated successfully.")
            return super().form_valid(form)
        else:
            messages.error(self.request, " No tables available for that time and group size.")
            return redirect("my_bookings")

    def get_success_url(self):
        return reverse_lazy("my_bookings")