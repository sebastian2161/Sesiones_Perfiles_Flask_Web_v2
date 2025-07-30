# 📱 Perfiles de sesiones Flask Web v2

Este proyecto es un sistema web que gestiona **sesiones de administración** y **perfiles de usuario**. Permite activar o desactivar módulos específicos que serán visibles para los usuarios en el portal web.

---

## 🚀 Tecnologías Utilizadas

| Tecnología | Descripción                           |
| ---------- | ------------------------------------- |
| Python     | Backend y lógica del servidor web     |
| Flask      | Framework web ligero basado en Python |
| Jinja2     | Motor de plantillas HTML              |
| HTML/CSS   | Estructura y estilos del frontend     |
| SQLite     | Base de datos local y ligera          |

---

## 🧩 Características Principales

### ✅ Módulo de Sesiones

- Inicio de sesión seguro para administradores.
- Autenticación con almacenamiento de sesiones.
- Control de acceso basado en roles.

### ✅ Módulo de Perfiles

- Creación y edición de perfiles de usuario.
- Activación y desactivación de módulos visibles.
- Visualización de configuraciones específicas por perfil.

### ✅ Panel Web Interactivo

- Portal accesible vía navegador web.
- Interfaz amigable desarrollada con HTML y CSS.
- Integración completa con Jinja2 y SQLite.

---

## 🚀 Instrucciones de Instalación Local

### 1. Clona el Repositorio

```bash
git clone https://github.com/sebastian2161/Sesiones_Perfiles_Flask_Web_v2.git
cd Sesiones_Perfiles_Flask_Web_v2
```

### 2. Crea un Entorno Virtual (opcional pero recomendado)

```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Instala las Dependencias

```bash
Librerias Python
```

### 4. Ejecuta la Aplicación

```bash
python run2.py
```

### 5. Abre el Navegador

```
http://127.0.0.1:3000
```

---

## 🌐 Despliegue en Producción (Cloud Run, Compute Engine, etc.)

- Crea un archivo `Dockerfile` si deseas desplegar como contenedor.
- Configura variables de entorno según corresponda.
- Puedes usar servicios como **Cloud Run**, **Heroku**, **Render**, etc.

---

## 📊 Base de Datos SQLite

- Archivo: `database.db`
- Se crea automáticamente al ejecutar por primera vez.
- Puedes explorarla con herramientas como DB Browser for SQLite.

---

## 🚫 Seguridad

- Se recomienda usar HTTPS en producción.
- Cambiar las claves secretas y tokens.
- Configurar autenticación fuerte para administradores.

---

## 👨‍💼 Autor y Repositorio

- GitHub: [Sessions\_Profiles\_Flask\_Web\_v2](https://github.com/sebastian2161/Sesiones_Perfiles_Flask_Web_v2)
- Desarrollador: [sebastian2161](https://github.com/sebastian2161)

---

## 📉 Recursos Adicionales

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Jinja2 Templates](https://jinja.palletsprojects.com/)
- [SQLite Docs](https://www.sqlite.org/docs.html)

---

## 🚧 Licencia

Este proyecto es de código abierto. Consulta el archivo LICENSE (si está disponible) para más información.
