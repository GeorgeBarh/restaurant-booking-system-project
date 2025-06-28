from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import MenuItem

class MenuListView(generic.ListView):
    model = MenuItem
    queryset = MenuItem.objects.all()
    template_name = "reservations/menu_list.html"
