from django.contrib import admin
from models import DishModel, DescriptionModel


# Register your models here.

@admin.register(DishModel)
class DishAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    fields = ('name',)


@admin.register(DescriptionModel)
class DescriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'dish')
    fields = ('dish', 'description', 'link')
