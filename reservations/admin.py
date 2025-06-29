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
    list_display = ('name', 'date', 'time', 'table')
    search_fields = ('name', 'email', 'phone')
    ordering = ('date', 'time')


