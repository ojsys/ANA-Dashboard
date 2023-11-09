from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dash'),
    path('', views.index, name='index'),
]