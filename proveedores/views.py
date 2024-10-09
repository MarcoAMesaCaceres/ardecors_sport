from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import Proveedor
from .forms import ProveedorForm
from django.core.exceptions import ValidationError
from insumos.models import Insumos
from proveedores.models import  Proveedor
def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'lista_proveedores.html', {'proveedores': proveedores})

def editar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            messages.success(request, "Proveedor actualizado exitosamente.")
            return redirect('lista_proveedores')
        else:
            messages.error(request, "Error al actualizar el proveedor. Por favor, revise los datos.")
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'editar_proveedor.html', {'form': form, 'proveedor': proveedor})

def crear_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Proveedor creado exitosamente.")
            return redirect('lista_proveedores')
        else:
            messages.error(request, "Error al crear el proveedor. Por favor, revise los datos.")
    else:
        form = ProveedorForm()
    return render(request, 'crear_proveedor.html', {'form': form})

def eliminar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        try:
            proveedor.delete()
            messages.success(request, "Proveedor eliminado exitosamente.")
            return redirect('lista_proveedores')
        except ValidationError as e:
            messages.error(request, str(e))
            return redirect('lista_proveedores')
    return render(request, 'eliminar_proveedor.html', {'proveedor': proveedor})