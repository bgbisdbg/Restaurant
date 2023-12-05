from django.db import models


class DishModel(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class DescriptionModel(models.Model):
    description = models.CharField(max_length=256)
    link = models.URLField(max_length=200, blank=True)
    dish = models.ForeignKey(to=DishModel, on_delete=models.CASCADE)
