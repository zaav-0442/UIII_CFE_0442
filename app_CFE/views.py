from django.shortcuts import render, redirect, get_object_or_404
from .models import Sucursal

def inicio_cfe(request):
    return render(request, 'inicio.html')

def agregar_sucursal(request):
    if request.method == 'POST':
        Sucursal.objects.create(
            nombre=request.POST['nombre'],
            clave=request.POST['clave'],
            direccion=request.POST['direccion'],
            telefono=request.POST['telefono'],
            ciudad=request.POST['ciudad'],
            estado=request.POST['estado'],
            fecha_apertura=request.POST['fecha_apertura']
        )
        return redirect('ver_sucursales')
    return render(request, 'sucursal/agregar_sucursal.html')

def ver_sucursales(request):
    sucursales = Sucursal.objects.all()
    return render(request, 'sucursal/ver_sucursales.html', {'sucursales': sucursales})

def actualizar_sucursal(request, id):
    sucursal = get_object_or_404(Sucursal, id=id)
    return render(request, 'sucursal/actualizar_sucursal.html', {'sucursal': sucursal})

def realizar_actualizacion_sucursal(request, id):
    sucursal = get_object_or_404(Sucursal, id=id)
    if request.method == 'POST':
        sucursal.nombre = request.POST['nombre']
        sucursal.clave = request.POST['clave']
        sucursal.direccion = request.POST['direccion']
        sucursal.telefono = request.POST['telefono']
        sucursal.ciudad = request.POST['ciudad']
        sucursal.estado = request.POST['estado']
        sucursal.fecha_apertura = request.POST['fecha_apertura']
        sucursal.save()
        return redirect('ver_sucursales')

def borrar_sucursal(request, id):
    sucursal = get_object_or_404(Sucursal, id=id)
    sucursal.delete()
    return redirect('ver_sucursales')
