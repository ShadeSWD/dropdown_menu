from django.contrib import admin
from menu.models import Menu


@admin.register(Menu)
class DealerAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'parent')

