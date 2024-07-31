from django.shortcuts import render, get_object_or_404, redirect, render
from .models import DetalleVenta
from .forms import DetalleVentaForm

def lista_detalles_venta(request):
    detalles = DetalleVenta.objects.all()
    return render(request, 'lista_detalles_venta.html', {'detalles': detalles})
def detalle_detalle_venta(request, detalle_id):
    detalle = get_object_or_404(DetalleVenta, id=detalle_id)
    return render(request, 'detalle_detalle_venta.html', {'detalle': detalle})

def crear_detalle_venta(request):
    if request.method == 'POST':
        form = DetalleVentaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = DetalleVentaForm()
    return render(request, 'crear_detalle_venta.html', {'form': form})

def eliminar_detalle_venta(request, pk):
    detalle = get_object_or_404(DetalleVenta, pk=pk)
    if request.method == 'POST':
        detalle.delete()
        return redirect('lista_detalles_venta')
    return render(request, 'eliminar_detalle_venta.html', {'detalle': detalle})