from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dash'),
    path('index/', views.index, name='index'),
]