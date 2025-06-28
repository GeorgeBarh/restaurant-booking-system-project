from django.contrib import admin
from .models import Table, Booking, MenuItem
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


@admin.register(MenuItem)
class MenuItemAdmin(SummernoteModelAdmin):
    list_display = ('name', 'price', 'status', 'created_on')
    search_fields = ('name', 'description')
    list_filter = ('status', 'created_on')
    summernote_fields = ('description',)