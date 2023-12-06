from django.urls import path
from menu.views import DescriptionListView, IndexView

app_name = 'menu'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('menu/', DescriptionListView.as_view(), name='menu')
]