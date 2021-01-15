from django.urls import path, include
from . import views

urlpatterns = [
    path('add', views.add, name='add'),
    path('<int:item_id>', views.detail, name='detail'),
]
