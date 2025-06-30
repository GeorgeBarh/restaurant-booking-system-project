from django.contrib import admin
from .models import MenuItem
from django_summernote.admin import SummernoteModelAdmin

@admin.register(MenuItem)
class MenuItemAdmin(SummernoteModelAdmin):
    list_display = ('name', 'price', 'category', 'status', 'created_on')
    search_fields = ('name', 'description')
    list_filter = ('category', 'status', 'created_on')
    summernote_fields = ('description',)
