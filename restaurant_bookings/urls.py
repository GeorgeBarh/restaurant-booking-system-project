from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("summernote/", include("django_summernote.urls")),
    path("", include("home.urls")),
    path("menu/", include("menu.urls")),
    path("reservations/", include("reservations.urls")),
    path("contact/", include("contact.urls")),
]