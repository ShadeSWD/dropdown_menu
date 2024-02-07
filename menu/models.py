from django.db import models


class Menu(models.Model):
    created_at = models.DateTimeField(verbose_name='creation date', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='change date', auto_now=True)
    name = models.CharField(verbose_name='element name', max_length=50)
    parent = models.ForeignKey('Menu', verbose_name='parent', blank=True, null=True, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'menu'
        verbose_name_plural = 'menus'

    def __str__(self):
        return f"{self.name}"
