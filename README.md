# Proyecto_Final
Proyecto Final de Ricardo Zegarra L.

Este proyecto fué realizado como parte del curso de Python en CoderHouse

## 🚀 Comenzando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

Consulte **[Implantação](#-implanta%C3%A7%C3%A3o)** para saber como implantar o projeto.

### 📋 Pré-requisitos

Esta aplicación fue desarrollada en Python utilizando Visual Studio Code para windows en una computadora con procesador de 64 bits.

- Se ha utilizado Python version 3.10.8
- Es necesario instalar Django versión 4.1.3

### 🔧 Instalación
Instalar Python igual o porterior a version 3.10.8
Instalar django igual o posterior a versión 4.1.3
Utilizar Visual Studio Code.

Descargar la aplicacion desde GitHub: https://github.com/rzegarral/proyecto_final.git

Posteriormente desde la Terminal deberá ejecutar: python manage.py runserver y se abrirá una ventana en el navegador parecido a: http://127.0.0.1:8000/

Aquí podra ejecutar las siguientes tres aplicaciones:

        1. Alta, baja, consulta y mantenimiento de Familiares

        http://127.0.0.1:8000/mi-familia/
        http://127.0.0.1:8000/mi-familia/buscar
        http://127.0.0.1:8000/mi-familia/alta
        http://127.0.0.1:8000/mi-familia/actualizar/<int:pk>
        http://127.0.0.1:8000/mi-familia/borrar/<int:pk>

        2. Alta, baja, consulta y mantenimiento de Amigos

        http://127.0.0.1:8000/mis-amigos/
        http://127.0.0.1:8000/mis-amigos/buscar_amigos
        http://127.0.0.1:8000/mis-amigos/alta
        http://127.0.0.1:8000/mis-amigos/actualizar/<int:pk>
        http://127.0.0.1:8000/mis-amigos/borrar-amigos/<int:pk>

        3. Alta, baja, consulta y mantenimiento de Autos

        http://127.0.0.1:8000/mis-autos/
        http://127.0.0.1:8000/mis-autos/buscar_auto
        http://127.0.0.1:8000/mis-autos/alta
        http://127.0.0.1:8000/mis-autos/actualizar/<int:pk>
        http://127.0.0.1:8000/mis-autos/borrar-auto/<int:pk>

También se tendrá acceso a la aplicación del siguiente Blog (Blog de Ricardo)

Ejecutando http://127.0.0.1:8000/blog-ricardo/ desde el navegador le aparecerá el siguiente menu:  

Inicio
Acerca de mi
Contacto
Registrarse
Ingresar

Aquí podrá ver los Post de ejemplo realizados
Podrá realizar el registro de un nuevo usuario, asignarle un avatar, crear un profile, dejar un mensaje
Podrá realizar el cambio de clave, de avatar y del profile de usuario.

Como super usuario podrá:
realizar nuevos Post; Estos se ordenaran cronológicamente del mas reciente hacia atrás.

Opcionalmente podrá ingresar directamente desde el navegador a traves de los siguientes links.
        http://127.0.0.1:8000/blog-ricardo/<int:pk>/detalle/ 
        http://127.0.0.1:8000/blog-ricardo/listar/ 
        http://127.0.0.1:8000/blog-ricardo/crear/ 
        http://127.0.0.1:8000/blog-ricardo/<int:pk>/borrar/ 
        http://127.0.0.1:8000/blog-ricardo/<int:pk>/actualizar/ 
        http://127.0.0.1:8000/blog-ricardo/signup/ 
        http://127.0.0.1:8000/blog-ricardo/login/ 
        http://127.0.0.1:8000/blog-ricardo/logout/ 
        http://127.0.0.1:8000/blog-ricardo/avatars/<int:pk>/actualizar/
        http://127.0.0.1:8000/blog-ricardo/users/<int:pk>/actualizar/
        http://127.0.0.1:8000/blog-ricardo/mensajes/crear/
        http://127.0.0.1:8000/blog-ricardo/mensajes/<int:pk>/detalle/
        http://127.0.0.1:8000/blog-ricardo/mensajes/listar/

Comprobará que los accesos de superusuario y usuario común están correctamente configurados a fin de mantener la seguridad del sitio.


## 🛠️ Desarrollado en Python

* framework web usado : Visual Studio Code
* Python version 3.10.8
* Django versión 4.1.3
* GitHub
* Windows 10 (64 bits)

## 📌 Versão

Usamos GitHub para control de versiones.   Para obtener la versión disponibles siga el siguiente link: https://github.com/rzegarral/proyecto_final.git

## ✒️ Autor

Ricardo Zegarra Lachapell

## 📄 Licença

Sin Licencia

## 🎁 Gratitud

* Profesor CoderHouse; Gerardo Martinez 📢;
* Tutor Coderhouse Carla Nazarena 🍺;
* Todo el equipo CoderHouse 🫂;

https://github.com/martinezger/proyecto-final.git