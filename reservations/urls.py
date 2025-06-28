from django.urls import path
from .views import MenuListView

urlpatterns = [
    path('', MenuListView.as_view(), name='home'),       # Homepage shows menu
    path('menu/', MenuListView.as_view(), name='menu'),  # Dedicated menu page
]