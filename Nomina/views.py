from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Inicio (request):

    return render(request,"Inicio.jinja")
def Listado(request):
    return render(request,"Listado.jinja")
