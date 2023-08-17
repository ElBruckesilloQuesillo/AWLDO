from django.urls import path

from lineaDeOro.views import *


urlpatterns = [
    path('',HomeView, name = 'Home'),
    path('comprar_boletos',BuyView, name = 'Buy'),
    path('rentar_unidad',RentView, name = 'Rent'),
    path('contacto',ContactView, name = 'Contact')
]