from .models import MenuItem
from django.views import generic

class MenuListView(generic.ListView):
    model = MenuItem
    template_name = "menu/index.html"
    context_object_name = "menu_items"
    paginate_by = 6

    def get_queryset(self):
        queryset = MenuItem.objects.filter(status=1).order_by("-created_on")
        category = self.request.GET.get("category")
        if category:
            queryset = queryset.filter(category=category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["selected_category"] = self.request.GET.get("category", "")
        return context
