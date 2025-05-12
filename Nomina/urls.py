#!/usr/bin/env python3
#
from django.urls import path
from .views import Inicio
urlpatterns = [
    path('Inicio/',Inicio,name="Inicio" )

]
