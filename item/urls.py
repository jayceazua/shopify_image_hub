from django.urls import path, include
from . import views

urlpatterns = [
    path('add', views.add, name='add'),
    path('search', views.search, name='search'),
    path('<int:item_id>/delete', views.delete, name='delete'),
    path('<int:item_id>', views.detail, name='detail'),
]
