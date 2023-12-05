from django.urls import path
from menu.views import DescriptionListView

app_name = 'menu'

urlpatterns = [
    path('menu/', DescriptionListView.as_view(), name='search')
]