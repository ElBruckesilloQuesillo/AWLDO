from django.http import HttpResponse
from django.template import Template, Context

#Importando render (para cargar plantillas) de una manera más rápida
from django.shortcuts import render


#Ejemplo de herencia
def InicioView(request):
    contexto = {
        "mensaje":"BIENVENIDO LINEADO DE ORO QUE ES DORADA"
        }
    
    return render(request, "InicioView.html", contexto)


