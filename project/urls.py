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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from ejemplo.views import (index, monstrar_familiares, BuscarFamiliar, AltaFamiliar, ActualizarFamiliar, BorrarFamiliar)
from ejemplo.views import (monstrar_amigos, BuscarAmigos, AltaAmigos, Amigosactualizar, BorrarAmigo)
from ejemplo.views import (monstrar_autos, BuscarAutos, AltaAutos, Autosactualizar, BorrarAuto)
from blog_ricardo.views import (index, PostList, PostCrear, PostDetalle, PostBorrar, PostActualizar, 
                                UserSignUp, UserLogin, UserLogout, AvatarActualizar, UserActualizar,
                                MensajeCrear, MensajeListar, MensajeDetalle )
from django.contrib.admin.views.decorators import staff_member_required

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
# blog_Ricardo
    path('blog-ricardo/', index, name="blog-ricardo-index" ), 
#    path('blog-ricardo/', index2, name="blog-ricardo-yo" ), 
#    path('blog-ricardo/yo/', YoDetalle.as_view(), name="blog-ricardo-yo"), 
    path('blog-ricardo/<int:pk>/detalle/', PostDetalle.as_view(), name="blog-ricardo-detalle" ), 
    path('blog-ricardo/listar/', PostList.as_view(), name="blog-ricardo-listar"), 
    path('blog-ricardo/crear/', staff_member_required(PostCrear.as_view()), name="blog-ricardo-crear"), 
    path('blog-ricardo/<int:pk>/borrar/', staff_member_required(PostBorrar.as_view()), name="blog-ricardo-borrar" ), 
    path('blog-ricardo/<int:pk>/actualizar/',staff_member_required(PostActualizar.as_view()), name="blog-ricardo-actualizar" ), 
    path('blog-ricardo/signup/', UserSignUp.as_view(), name="blog-ricardo-signup" ),
    path('blog-ricardo/login/', UserLogin.as_view(), name="blog-ricardo-login" ),
    path('blog-ricardo/logout/', UserLogout.as_view(), name="blog-ricardo-logout" ),
    path('blog-ricardo/avatars/<int:pk>/actualizar/', AvatarActualizar.as_view(), name="blog-ricardo-avatars-actualizar" ),

    path('blog-ricardo/users/<int:pk>/actualizar/', UserActualizar.as_view(), name="blog-ricardo-users-actualizar"),
    path('blog-ricardo/mensajes/crear/', MensajeCrear.as_view(), name="blog-ricardo-mensajes-crear"),
    path('blog-ricardo/mensajes/<int:pk>/detalle/', MensajeDetalle.as_view(), name="blog-ricardo-mensajes-detalle"),
    path('blog-ricardo/mensajes/listar/', MensajeListar.as_view(), name="blog-ricardo-mensajes-listar"),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)