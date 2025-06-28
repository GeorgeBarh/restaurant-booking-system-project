from django.views import generic
from .models import MenuItem


class MenuListView(generic.ListView):
    queryset = MenuItem.objects.filter(status=1)
    template_name = "menu_list.html"
