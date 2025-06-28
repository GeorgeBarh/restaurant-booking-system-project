from django.contrib import admin
from .models import Table, Booking, MenuItem
from django_summernote.admin import SummernoteModelAdmin



@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('table_number', 'capacity')
    ordering = ('table_number',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'time', 'guests', 'table', 'status')
    list_filter = ('status', 'date', 'time')
    search_fields = ('user__username',)
    ordering = ('date', 'time')


@admin.register(MenuItem)
class MenuItemAdmin(SummernoteModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)
    summernote_fields = ('description',)
