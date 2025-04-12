# Definición de Alcance de Solución de  Plataforma de Microblogging

## 1. Identificación del Problema
Desarrollo de una plataforma web de microblogging que permita a los usuarios compartir mensajes cortos, interactuar y conectarse entre sí, con funcionalidades similares a las de Twitter/X.

## 2. Situaciones y Casos Especiales

### Casos de Usuarios
- Registro e inicio de sesión de usuarios
- Perfiles con diferentes configuraciones de privacidad
- Usuarios con roles distintos (estándar, verificados, administradores)

### Casos de Publicaciones
- Creacion de publicacion
- Publicaciones con menciones a otros usuarios
- Publicaciones con imagenes limitadas
- Manejo de contenido inapropiado

### Casos de Interacción
- Sistema de likes y comentarios
- Reposts
- Seguimiento de usuarios
- Bloqueo a usuarios

## 3. Establecimiento de Alcances

### Limitaciones de la Solución
La plataforma NO podrá:
1. Realizar transmisiones en vivo
2. Integrar sistema de mensajería directa complejo
3. Crear funcionalidades de monetización
4. Implementar publicidad personalizada
5. Implementar un algoritmo de recomendación avanzado

### Restricciones Técnicas
- Límite de caracteres por publicación
- Capacidad inicial de registro para 10,000 usuarios
- Compatible con navegadores web modernos
- Almacenamiento limitado de contenido multimedia


## Módulos principales

Todos los datos se guardan en una base de datos.

### Gestión de Usuarios

#### Registro

Se van a pedir datos básicos:
- Mail
- Nombre de usuario
- Contraseña

se valida que no exista una cuenta con el mismo nombre de usuario, y si esto es verdadero, se registra la nueva cuenta.

#### Publicación de contenido

Los posts tendrán un límite de caracteres. Si supera el límite, se muestra un error al usuario. Se le permite al usuario cargar una cantidad máxima de archivos multimedia. El usuario podrá mencionar a otros usuarios y estos serán notificados al crearse la publicación.

#### Interacciones

La plataforma va a tener 3 tipos de interacciones: likes, comentarios y reposts.

#### Moderación de contenido

Cuando un usuario crea una publicacion, se evalua si el contenido es apropiado y, si no lo es, se elimina la misma y se reporta el usuario.

## 6. Reflexión

### Importancia de la definición de alcance

Un alcance bien definido es una excelente manera de documentar una solución y muchas veces ayuda a descubrir casos que no se contemplaron previamente a medida que el alcance va madurando en sus definiciones.
