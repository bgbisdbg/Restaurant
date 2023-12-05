# menu/urls.py
from django.urls import path
from . import views
from menu.views import DescriptionListView

app_name = 'menu'

urlpatterns = [
    path('', DescriptionListView.as_view(), name='menu')
]