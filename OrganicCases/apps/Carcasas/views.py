from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from .models import Carcasa, Material
from .forms import FormularioModificarCarcasa
from django.urls import reverse_lazy

from rest_framework import generics
from .serializers import CarcasaSerializer, MaterialSerializer

# ------------- importacines API ---------------------
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser

# Create your views here.


class ListaCarcasas(ListView):
    # Leer todos
    model = Carcasa
    template_name = 'Carcasas/principal.html'


class DetalleCarcasa(DetailView):
    # Leer uno en especial
    model = Carcasa
    template_name = 'Carcasas/detalle.html'


class EliminarCarcasa(DeleteView):
    # Eliminar uno
    model = Carcasa
    template_name = 'Carcasas/eliminar.html'
    success_url = reverse_lazy('principal_carcasas')


class ModificarCarcasa(UpdateView):
    # Modificar uno
    model = Carcasa
    form_class = FormularioModificarCarcasa
    template_name = 'Carcasas/modificar.html'

    def get_success_url(self):
        # Devolverse a la pantalla de detalle si es que fue modificado exitosamente
        return reverse_lazy('detalle_carcasa', kwargs={'pk': self.object.id})


class CrearCarcasa(CreateView):
    # Crear uno
    model = Carcasa
    fields = ['nombre', 'descripcion', 'material', 'modeloEquipo']
    template_name = 'Carcasas/crear.html'

    def get_success_url(self):
        # Devolverse a la pantalla principal si se pudo crear una carcasa
        return reverse_lazy('principal_carcasas')

    def form_valid(self, form):
        # Agregar el usuario a la propiedad creador, si es que el formulario es válido.
        form.instance.creador = self.request.user
        return super(CrearCarcasa, self).form_valid(form)


def buscar_carcasas(request):
    # Buscar según filtro
    lista = Carcasa.objects.all()
    nombre_material = request.GET.get('nombre-material')
    nombre_modelo = request.GET.get('nombre-modelo')

    if 'btn-buscarMaterial' in request.GET:
        if nombre_material:
            lista = Carcasa.objects.filter(
                material__nombre__icontains=nombre_material)
    elif 'btn-buscarModelo' in request.GET:
        if nombre_modelo:
            lista = Carcasa.objects.filter(
                modeloEquipo__nombre__icontains=nombre_modelo)

    data = {
        'object_list': lista
    }
    return render(request, 'Carcasas/filtro.html', data)


class API_objects(generics.ListCreateAPIView):
    queryset = Carcasa.objects.all()
    serializer_class = CarcasaSerializer


class API_objects_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Carcasa.objects.all()
    serializer_class = CarcasaSerializer


@api_view(['GET', 'POST'])
def material_collection(request):
    if request.method == 'GET':
        materiales = Material.objects.all()
        serializer = MaterialSerializer(materiales, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MaterialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Si el proceso de deserialización funciona, devolvemos una respuesta con un código 201 (creado
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # si falla el proceso de deserialización, devolvemos una respuesta 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def material_element(request, pk):
    material = get_object_or_404(Material, id=pk)

    if request.method == 'GET':
        serializer = MaterialSerializer(material)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        material.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':

        serializer = MaterialSerializer(material, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
