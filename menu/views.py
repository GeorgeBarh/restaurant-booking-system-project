from django.views import generic
from .models import MenuItem

# Displays a list of available menu items, filtered by category and paginated
class MenuListView(generic.ListView):
    model = MenuItem
    template_name = "menu/index.html"
    context_object_name = "menu_items"
    paginate_by = 6

    def get_queryset(self):
        # Get all available items, filter by category if selected
        queryset = MenuItem.objects.filter(status=1).order_by("-created_on")
        category = self.request.GET.get("category")
        if category:
            queryset = queryset.filter(category=category)
        return queryset

    def get_context_data(self, **kwargs):
        # Add selected category to context for template button highlighting
        context = super().get_context_data(**kwargs)
        context["selected_category"] = self.request.GET.get("category", "")
        return context

