from django.contrib import admin
from django.urls import path, include

# Main URL configuration for the project, including all apps and admin
urlpatterns = [
    path("admin/", admin.site.urls),
    path("summernote/", include("django_summernote.urls")),
    path("", include("home.urls")),
    path("menu/", include("menu.urls")),
    path("reservations/", include("reservations.urls")),
    path("contact/", include("contact.urls")),
    path("accounts/", include("allauth.urls")),  # Login, Signup, Logout
]
