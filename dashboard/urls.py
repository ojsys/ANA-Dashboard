from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('farmers/', views.farmers, name='farmers'),
    path('add_farmer/', views.add_farmer, name='add_farmer'),
]