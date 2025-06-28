from django.views import generic
from .models import MenuItem

class MenuListView(generic.ListView):
    model = MenuItem
    queryset = MenuItem.objects.filter(status=1).order_by('name')  # Only available items
    template_name = 'menu_list.html'