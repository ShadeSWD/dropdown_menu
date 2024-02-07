from django.db import models


class MenuItem(models.Model):
    created_at = models.DateTimeField(verbose_name='creation date', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='change date', auto_now=True)
    name = models.CharField(verbose_name='element name', max_length=50)
    menu = models.ForeignKey('Menu', verbose_name='menu', on_delete=models.PROTECT)
    parent = models.ForeignKey('MenuItem', verbose_name='parent item', blank=True, null=True, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'menu item'
        verbose_name_plural = 'menu items'

    def __str__(self):
        return f"{self.name}"


class Menu(models.Model):
    created_at = models.DateTimeField(verbose_name='creation date', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='change date', auto_now=True)
    name = models.CharField(verbose_name='element name', max_length=50)

    class Meta:
        verbose_name = 'menu'
        verbose_name_plural = 'menus'

    def __str__(self):
        return f"{self.name}"

    @property
    def menu_items(self):
        return MenuItem.objects.filter(menu=self.pk)
