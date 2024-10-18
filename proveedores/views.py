from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import Proveedor
from .forms import ProveedorForm
from django.core.exceptions import ValidationError
from insumos.models import Insumos
from proveedores.models import  Proveedor
def lista_proveedores(request):
    id_query = request.GET.get('id', '')
    nombre_query = request.GET.get('nombre', '')
    telefono_query = request.GET.get('telefono', '')
    email_query = request.GET.get('email', '')
    direccion_query = request.GET.get('direccion', '')

    # Validación del ID
    if id_query and not id_query.isdigit():
        messages.error(request, "Debe colocar un número válido para el ID.")
        return render(request, 'lista_proveedores.html', {'proveedores': Proveedor.objects.none()})

    proveedores = Proveedor.objects.all()

    if id_query:
        proveedores = proveedores.filter(id=id_query)
    if nombre_query:
        proveedores = proveedores.filter(nombre__icontains=nombre_query)
    if telefono_query:
        proveedores = proveedores.filter(telefono__icontains=telefono_query)
    if email_query:
        proveedores = proveedores.filter(email__icontains=email_query)
    if direccion_query:
        proveedores = proveedores.filter(direccion__icontains=direccion_query)

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