from django.shortcuts import render, HttpResponse

from .models import *

#Inicio
def HomeView(request):

    return render(request, 'lineaDeOro/HomeView.html')

#Comprar
def BuyView(request):

    ciudades = Ciudad.objects.all()
    destinos = Destino.objects.all()
    return render(request, 'lineaDeOro/BuyView.html', {'Ciudades':ciudades, 'Destinos':destinos})

#Rentar unidad
def RentView(request):

    return render(request, 'lineaDeOro/RentView.html')

#Contacto
def ContactView(request):

    return render(request, 'lineaDeOro/ContactView.html')