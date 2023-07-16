# MotoBlog

MotoBlog es un sitio web dedicado a las motocicletas. Aquí encontrarás reseñas detalladas y especificaciones técnicas de diferentes modelos de motocicletas, así como información relacionada.

## Funcionalidades

### Blog
- Visualización de Publicaciones: Puedes navegar por la lista de publicaciones existentes y leer su contenido completo.
- Creación de Publicaciones: Si estás registrado y autenticado, puedes crear nuevas publicaciones para compartir tus reseñas.
- Edición y Eliminación de Publicaciones: También puedes editar y eliminar las publicaciones que has creado previamente.
- URLs:
    'posts/', 
    'postcreate/', 
    'posts/ID/', 
    'posts/ID/update/', 
    'posts/ID/delete/' 

### Users
- Visualización de Publicaciones: Puedes navegar por la lista de publicaciones existentes y leer su contenido completo.
- Creación de Publicaciones: Si estás registrado y autenticado, puedes crear nuevas publicaciones para compartir tus reseñas.
- Edición y Eliminación de Publicaciones: También puedes editar y eliminar las publicaciones que has creado previamente.
- URLs:
    'login/', 
    'logout/', 
    'register/', 
    'profile/', 
    'profile/changePassword', 
    'profile/deleteUser', 
    'profile/deleteAvatar' 

## Tecnologías Utilizadas

- Django: Marco de desarrollo web utilizado para construir la aplicación.
- HTML/CSS: Lenguajes de marcado y estilos utilizados para la presentación y diseño de las páginas.
- Bootstrap: Marco de CSS utilizado para agregar estilos y componentes responsivos al sitio.

## Instalación

1. Clona el repositorio de MotoBlog en tu máquina local.
2. Instala summernote `pip install django-summernote`.
3. Aplica las migraciones ejecutando el siguiente comando: `python manage.py migrate`.
4. Inicia el servidor de desarrollo con el siguiente comando: `python manage.py runserver`.

¡Eso es todo! Ahora puedes acceder al sitio web desde tu navegador ingresando la URL proporcionada por el servidor de desarrollo.


## Autor

Este proyecto fue desarrollado por Roman Valverde y Gabriel Aquino como entrega final de la Comisión 54485 del curso de Python & Django en Coderhouse.
