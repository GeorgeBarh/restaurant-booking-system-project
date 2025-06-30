from django.contrib import admin
from .models import Table, Booking
from menu.models import MenuItem
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('number', 'seats')
    ordering = ('number',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "date", "time", "guests", "table", "phone", "notes")
    list_filter = ("date", "table")
    search_fields = ("user__username", "name", "email", "phone", "notes")
    ordering = ("date", "time")
