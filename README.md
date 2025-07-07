**ServiciosConstruccion** es una aplicación web desarrollada en **Python con Django**, pensada como un portal de empleo para el rubro de la construcción. Profesionales pueden publicar sus servicios y los usuarios pueden buscar trabajadores para arreglos, refacciones y obras.



## ✨ Características

✅ Registro e inicio de sesión de usuarios  
✅ Perfiles personalizados con imagen, descripción y sitio web  
✅ Creación, edición y eliminación de publicaciones (tipo blog)  
✅ Visualización de servicios ofrecidos  
✅ Barra de navegación dinámica (cambia si estás logueado o no)  
✅ Panel de administración de Django para gestión de contenido  



## 🚀 Cómo ejecutar el proyecto

### ⚙️ Clonar el repositorio

git clone https://github.com/TuUsuario/ServiciosConstruccion.git
cd ServiciosConstruccion

🐍 Crear entorno virtual

python -m venv env

▶️ Activar entorno virtual

env\Scripts\activate        # Windows
source env/bin/activate     # Linux/macOS


📦 Instalar dependencias

pip install -r requirements.txt


🗃️ Migrar la base de datos

python manage.py migrate


🔐 Crear superusuario (opcional para admin)

python manage.py createsuperuser


💻 Ejecutar el servidor local

python manage.py runserver
📍 Accedé a: http://127.0.0.1:8000



📂 Estructura del Proyecto

ServiciosConstruccion/
├── accounts/           # Registro, login y perfil de usuarios
├── pages/              # Blog de publicaciones
├── servicios/          # Servicios ofrecidos por usuarios
├── static/             # Archivos estáticos (CSS, JS, imágenes)
├── templates/          # Plantillas HTML
└── media/              # Archivos subidos (avatares, imágenes de perfil)

🧑‍🎓 Autor
Maxi Pérez
Trabajo final del curso de Python con Django
📎 GitHub: https://github.com/Maxi912/ServiciosConstruccion.git

