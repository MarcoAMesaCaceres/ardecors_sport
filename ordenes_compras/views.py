from django.shortcuts import render, get_object_or_404
from .models import OrdenCompra
from .forms import OrdenCompraForm

def lista_ordenes_compra(request):
    ordenes = OrdenCompra.objects.all()
    return render(request, 'ordenes_compra/lista_ordenes_compra.html', {'ordenes': ordenes})

def detalle_orden_compra(request, orden_id):
    orden = get_object_or_404(OrdenCompra, id=orden_id)
    return render(request, 'ordenes_compra/detalle_orden_compra.html', {'orden': orden})

def crear_orden_compra(request):
    if request.method == 'POST':
        form = OrdenCompraForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = OrdenCompraForm()
    return render(request, 'ordenes_compra/crear_orden_compra.html', {'form': form})