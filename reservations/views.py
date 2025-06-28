from django.views import generic
from django.shortcuts import render
from .models import MenuItem

class MenuListView(generic.ListView):
    model = MenuItem
    queryset = MenuItem.objects.filter(status=1).order_by('-created_on')
    template_name = "reservations/index.html"  # Updated path
    context_object_name = 'menu_list'
    paginate_by = 6 