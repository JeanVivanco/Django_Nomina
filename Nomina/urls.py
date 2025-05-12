#!/usr/bin/env python3
#
from django.urls import path
from .views import Inicio,Listado
urlpatterns = [
    path('Inicio/',Inicio,name="Inicio" ),
    path('Listado/',Listado,name="Listado"),
]
