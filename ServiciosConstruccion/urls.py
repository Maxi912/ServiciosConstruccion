"""
URL configuration for ServiciosConstruccion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Rutas de pages/blog
    path('', include('pages.urls')),

    # Rutas de usuarios (signup, login, logout, profile)
    path('accounts/', include('accounts.urls')),

    # Rutas de servicios (lista y creación de servicios)
    path('servicios/', include('servicios.urls')),  # <-- AGREGAR esta línea
]

# Para servir en desarrollo los archivos subidos (imágenes de perfil, etc.)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)