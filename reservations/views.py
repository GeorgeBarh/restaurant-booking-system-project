from django.views.generic.edit import CreateView
from .models import Booking

class BookTableView(CreateView):
    model = Booking
    fields = ['name', 'email', 'phone', 'date', 'time', 'table']
    template_name = "reservations/book_table.html"
    success_url = "/reservations/?success=true"