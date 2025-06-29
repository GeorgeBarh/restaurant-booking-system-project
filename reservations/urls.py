from django.urls import path
from . import views

urlpatterns = [
    path("book/", views.BookTableView.as_view(), name="book_table"),
    path("my-bookings/", views.MyBookingsView.as_view(), name="my_bookings"),
]