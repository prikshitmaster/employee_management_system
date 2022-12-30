from django.contrib import admin
from django.urls import path, include

from base import views

urlpatterns = [
        path('', views.home , name='home'),
        path('all-employes', views.allEmployee , name='all-employes'),
        path('add-employes', views.addEmployee , name='add-employes'),
        path('remove-employes/<str:pk>', views.removeEmployee , name='remove-employes'),
        path('filter-employes', views.filterEmployee , name='filter-employes'),
]
