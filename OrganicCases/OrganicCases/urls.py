"""OrganicCases URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

# Importamos para definir los archivos MEDIA o imgs subidas
from django.conf.urls.static import static
from django.conf import settings
# Importamos vistas de autenticación
from django.contrib.auth import views as autenticacion

urlpatterns = [
    path('admin/', admin.site.urls),

    # Vistas de nuestras aplicaciones
    path('', include('apps.Carcasas.urls'), name='carcasas_url'),
    path('usuario/', include('apps.Usuarios.urls'), name='usuarios'),
    # path('trabajador/', include('apps.Trabajadores.urls'), name='trabajadores'),

    # Vistas de autenticación
    path('login/', autenticacion.LoginView.as_view(
        redirect_authenticated_user=True,
        template_name='Usuarios/login.html'), name='login'),
    path('logout/', autenticacion.LogoutView.as_view(
        template_name='Usuarios/logout.html'), name='logout'),

    # Vistas de autenticación FB
    path('', include('social_django.urls', namespace='social')),

    # PWA
    path('', include('pwa.urls')),

]

# Definimos carpeta donde estarán nuestros archivos MEDIA
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
