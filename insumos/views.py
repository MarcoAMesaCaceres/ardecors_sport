from django.shortcuts import render, get_object_or_404, redirect
from .models import Insumos
from .forms import InsumosForm
from django.db.models import Q
from django.contrib import messages
from django.core.exceptions import ValidationError
from proveedores.models import  Proveedor

def lista_insumos(request):
    id_query = request.GET.get('id', '')
    nombre_query = request.GET.get('nombre', '').strip()
    descripcion_query = request.GET.get('descripcion', '').strip()
    proveedor_query = request.GET.get('proveedor', '').strip()
    precio_query = request.GET.get('precio', '').strip()
    stock_query = request.GET.get('stock', '').strip()

    # Validación del ID
    if id_query and not id_query.isdigit():
        messages.error(request, "Debe colocar un número válido para el ID.")
        return render(request, 'lista_insumos.html', {'insumos': Insumos.objects.none()})

    insumos = Insumos.objects.all()

    if id_query:
        insumos = insumos.filter(id=id_query)
    if nombre_query:
        insumos = insumos.filter(nombre__icontains=nombre_query)
    if descripcion_query:
        insumos = insumos.filter(descripcion__icontains=descripcion_query)
    if proveedor_query:
        # Asegúrate de que 'nombre' sea el campo correcto del modelo Proveedor
        insumos = insumos.filter(proveedor__nombre__icontains=proveedor_query)
    if precio_query:
        try:
            precio_value = float(precio_query)
            insumos = insumos.filter(precio=precio_value)
        except ValueError:
            messages.error(request, "El precio debe ser un número válido.")
    if stock_query:
        try:
            stock_value = int(stock_query)
            insumos = insumos.filter(stock=stock_value)
        except ValueError:
            messages.error(request, "El stock debe ser un número válido.")

    return render(request, 'lista_insumos.html', {'insumos': insumos})


def crear_insumos(request):
    if request.method == 'POST':
        form = InsumosForm(request.POST, request.FILES)
        if form.is_valid():
            insumos = form.save()
            return redirect('lista_insumos')
    else:
        form = InsumosForm()
    return render(request, 'crear_insumos.html', {'form': form})
def editar_insumos(request, pk):
    insumos = get_object_or_404(Insumos, pk=pk)
    if request.method == 'POST':
        form = InsumosForm(request.POST, instance=insumos)
        if form.is_valid():
            form.save()
            messages.success(request, 'El insumo ha sido actualizado exitosamente.')
            return redirect('lista_insumos')
        else:
            messages.error(request, 'Ha ocurrido un error al actualizar el insumo. Por favor, revise los campos.')
    else:
        form = InsumosForm(instance=insumos)
    return render(request, 'editar_insumos.html', {'form': form, 'insumos': insumos})

def eliminar_insumos(request, pk):
    insumos = get_object_or_404(Insumos, pk=pk)
    if request.method == 'POST':
        try:
            insumos.delete()
            messages.success(request, 'El insumo ha sido eliminado exitosamente.')
            return redirect('lista_insumos')
        except ValidationError as e:
            messages.error(request, str(e))
            return redirect('lista_insumos')
    return render(request, 'eliminar_insumos.html', {'insumos': insumos})