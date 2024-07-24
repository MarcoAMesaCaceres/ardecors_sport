from django.shortcuts import render, get_object_or_404
from .models import Proveedor
from .forms import ProveedorForm

def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedores/lista_proveedores.html', {'proveedores': proveedores})

def detalle_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    return render(request, 'proveedores/detalle_proveedor.html', {'proveedor': proveedor})

def crear_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProveedorForm()
    return render(request, 'proveedores/crear_proveedor.html', {'form': form})
