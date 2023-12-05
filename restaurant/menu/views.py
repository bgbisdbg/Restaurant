from django.shortcuts import render
from django.views.generic import ListView

from menu.models import DescriptionModel


# Create your views here.


class DescriptionListView(ListView):
    model = DescriptionModel
    template_name = 'menu/menu.html'
    title = "Меню"
