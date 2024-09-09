from django.shortcuts import get_object_or_404, redirect, render
from .models import Proveedor
from .forms import ProveedorForm

def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'lista_proveedores.html', {'proveedores': proveedores})

def editar_proveedor(request, pk):
    proveedores = get_object_or_404(proveedores, pk=pk)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedores)
        if form.is_valid():
            form.save()
            return redirect('lista_ventas')
    else:
        form = ProveedorForm(instance=proveedores)
    return render(request, 'editar_proveedor.html', {'form': form, 'proveedores': proveedores})


def crear_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProveedorForm()
    return render(request, 'crear_proveedor.html', {'form': form})

def eliminar_proveedor(request, pk):
    Proveedores = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        Proveedores.delete()
        return redirect('lista_ventas')
    return render(request, 'eliminar_proveedor.html', {'Proveedores': Proveedores})