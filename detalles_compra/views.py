from django.shortcuts import render, get_object_or_404, redirect
from .models import DetalleOrdenCompra
from .forms import DetalleOrdenCompraForm
from .models import DetalleCompra

def lista_detalles_compra(request):
    detalles = DetalleOrdenCompra.objects.all()
    return render(request, 'lista_detalles_compra.html', {'detalles': detalles})

def detalle_detalle_compra(request, detalle_id):
    detalle = get_object_or_404(DetalleOrdenCompra, id=detalle_id)
    return render(request, 'detalle_detalle_compra.html', {'detalle': detalle})

def crear_detalle_compra(request):
    if request.method == 'POST':
        form = DetalleOrdenCompraForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = DetalleOrdenCompraForm()
    return render(request, 'crear_detalle_compra.html', {'form': form})


def eliminar_detalle_compra(request, pk):
    detalle = get_object_or_404(DetalleCompra, pk=pk)
    if request.method == 'POST':
        detalle.delete()
        return redirect('lista_detalles_compra')
    return render(request, 'eliminar_detalles_compra.html', {'detalle': detalle})