from django.views import generic
from reservations.models import MenuItem

class MenuListView(generic.ListView):
    model = MenuItem
    template_name = "menu/index.html"
    context_object_name = "menu_items"
    paginate_by = 6

    def get_queryset(self):
        return MenuItem.objects.filter(status=1).order_by("-created_on")
