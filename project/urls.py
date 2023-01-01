"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
#from ejemplo.views import index, saludar_a, sumar
from ejemplo.views import index, monstrar_familiares

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/', index), # ESTA ES LA NUEVA FUNCTION
#    path('saludar-a/<nombre>/', saludar_a),
#    path('sumar/<int:a>/<int:b>/', sumar),
    path('mi-familia/', monstrar_familiares), # nueva vista
]  
"""

from django.contrib import admin
from django.urls import path
from ejemplo.views import (index, monstrar_familiares, BuscarFamiliar, AltaFamiliar, ActualizarFamiliar, BorrarFamiliar)
from ejemplo.views import (monstrar_amigos, BuscarAmigos, AltaAmigos, Amigosactualizar, BorrarAmigo)
from ejemplo.views import (monstrar_autos, BuscarAutos, AltaAutos, Autosactualizar, BorrarAuto)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/', index),
    path('mi-familia/', monstrar_familiares),  # VISTA BASADA EN UNA FUNCION
    path('mi-familia/buscar', BuscarFamiliar.as_view()),  #VISTA BASADA EN UNA CLASE
    path('mi-familia/alta', AltaFamiliar.as_view()),
    path('mi-familia/actualizar/<int:pk>', ActualizarFamiliar.as_view()),
    path('mi-familia/borrar/<int:pk>', BorrarFamiliar.as_view()),
# ruta para Amigos
    path('mis-amigos/', monstrar_amigos),
    path('mis-amigos/buscar_amigos', BuscarAmigos.as_view()),
    path('mis-amigos/alta', AltaAmigos.as_view()),
    path('mis-amigos/actualizar/<int:pk>', Amigosactualizar.as_view()),
    path('mis-amigos/borrar-amigos/<int:pk>', BorrarAmigo.as_view()), 
# ruta para Autos
    path('mis-autos/', monstrar_autos),
    path('mis-autos/buscar_auto', BuscarAutos.as_view()),
    path('mis-autos/alta', AltaAutos.as_view()),
    path('mis-autos/actualizar/<int:pk>', Autosactualizar.as_view()),
    path('mis-autos/borrar-auto/<int:pk>', BorrarAuto.as_view()), 
]
