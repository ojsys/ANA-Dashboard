from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('farmers/', views.farmers, name='farmers'),
    path('add_farmer/', views.add_farmer, name='add_farmer'),
    path('eas/', views.our_eas, name='our_eas'),
    path('new_eas/', views.eas, name='new_eas'),
    path('add_ea/', views.add_eas, name='add_ea'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)