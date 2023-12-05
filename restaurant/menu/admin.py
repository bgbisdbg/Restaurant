from django.contrib import admin
from menu.models import DishModel, DescriptionModel


@admin.register(DishModel)
class DishAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    fields = ('name',)


@admin.register(DescriptionModel)
class DescriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'dish')
    fields = ('dish', 'description', 'link')
