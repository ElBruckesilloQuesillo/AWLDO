"""lineaDeOro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path



#Importando todos nuestros métodos de carga y renderizado.
from lineaDeOro.views import *

"""
urlpatterns es una lista de patrones, cada elemento de esta lista define una url y un método
asociado a esta url. Ejemplo:
    Cada vez que se ingrese en el navegador la url 'lineaDeOro/ejemplo', se llamará el método 
    EjemploView.
"""

urlpatterns = [
    path('lineaDeOro/ejemplo', EjemploView),
]
