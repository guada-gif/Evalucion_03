from django.urls import path
from .views import ListaCarcasas, DetalleCarcasa, EliminarCarcasa, ModificarCarcasa, CrearCarcasa, buscar_carcasas, API_objects, API_objects_details, material_element, material_collection
from django.contrib.auth.views import login_required
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # Leer todos
    path('', ListaCarcasas.as_view(), name='principal_carcasas'),
    # Leer uno en especial
    path('carcasa/<int:pk>/', DetalleCarcasa.as_view(), name='detalle_carcasa'),
    # Eliminar uno
    path('carcasa/eliminar/<int:pk>',
         login_required(EliminarCarcasa.as_view()), name='eliminar_carcasa'),
    # Modificar uno
    path('carcasa/modificar/<int:pk>', login_required(ModificarCarcasa.as_view()),
         name='modificar_carcasa'),
    # Crear uno
    path('carcasa/crear', login_required(CrearCarcasa.as_view()),
         name='crear_carcasa'),
    # Buscar todos
    path('carcasa/buscar', buscar_carcasas, name='buscar_carcasas'),
    # API carcasas
    path('api/', API_objects.as_view()),
    path('api/<int:pk>/', API_objects_details.as_view()),
    # API materiales
    path('api-materiales/',  material_collection, name='material_collection'),
    path('api-materiales/<int:pk>/', material_element, name='material_element')


]
urlpatterns = format_suffix_patterns(urlpatterns)
