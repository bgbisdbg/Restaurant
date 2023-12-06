from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from menu.models import DescriptionModel


# Create your views here.

class IndexView(TemplateView):
    template_name = 'menu/index.html'


class DescriptionListView(ListView):
    model = DescriptionModel
    template_name = 'menu/menu.html'
    title = "Меню"
