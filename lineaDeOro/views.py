"""
Aquí se incluirán los métodos de carga y renderizado de vistas html.
Cada método se llamará dependiendo la url asociada a este, esa configuración se 
aloja en el archivo urls.py

Nomenclatura de métodos para mayor entendimiento:
    Si mi vista se llama 'InicioView', llamar al método de la misma manera.
"""

from django.http import HttpResponse
from django.template import Template, Context

#Importando render (para cargar vistas) de una manera más rápida
from django.shortcuts import render


#Vista Ejemplo. Recibe como parámetro la petición del navegador.
def EjemploView(request):
    """
    Cada método retorna en su llamado una vista renderizada en html con la ayuda de la función 
    render()... este requiere 3 parámetros básicos para funcionar.
        
        1. request: Es la petición del navegador, este es OBLIGATORIO y siempre va.
        2. vista html: Sólo hay que ingresar el nombre de la vista a mostrar, estas se
            encuentran alojadas en la carpeta views.
        3. contexto: Este no es obligatorio. El contexto es un diccionario de parametros que Django
            utilizará para visualizar información en la vista. Por ejemplo, puedo mandar información
            de un autobús estructurada en un diccionario y mostrar esos datos en mi vista html.

        render(request , 'MiVista.html' , contexto)
    """

    #Suponiendo que mostraremos en la vista información de un autobús
    contexto = {
        "capacidad_autobus" : 50,
        "placas_autobus" : "AKJ-89",
        "nombre_chofer" : "Luisillo",
        "apellido_chofer" : "El pillo"
        }

    #Retornamos solicitud, nuestra plantilla renderizada y el contexto. Ver vista EjemploView.
    return render(request, "EjemploView.html", contexto) 


#Vista inicio
def InicioView(request):
    contexto = {}
    return render(request,'InicioView.html', contexto)
