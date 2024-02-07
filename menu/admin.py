from django.contrib import admin
from menu.models import Menu, MenuItem


@admin.register(Menu)
class DealerAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


@admin.register(MenuItem)
class DealerAdmin(admin.ModelAdmin):
    list_display = ('pk', 'menu', 'name', 'parent')
    list_filter = ('menu',)
