from django.urls import path
from . import views
from .views import BookTableView, MyBookingsView, cancel_booking,UpdateBookingView

# All reservation-related routes: book, edit, cancel, view bookings
urlpatterns = [
    path("book/", views.BookTableView.as_view(), name="book_table"),
    path("my-bookings/", views.MyBookingsView.as_view(), name="my_bookings"),
    path("cancel/<int:pk>/", cancel_booking, name="cancel_booking"),
    path("edit/<int:pk>/", UpdateBookingView.as_view(), name="edit_booking"),
]