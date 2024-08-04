from django.shortcuts import render, get_object_or_404, redirect, render
from .models import DetalleVenta
from .forms import DetalleVentaForm

def lista_detalles_venta(request):
    detalles = DetalleVenta.objects.all()
    return render(request, 'lista_detalles_venta.html', {'detalles': detalles})

def editar_detalle_venta(request, pk):
    detalles = get_object_or_404(detalles, pk=pk)
    if request.method == 'POST':
        form = DetalleVentaForm(request.POST, instance=detalles)
        if form.is_valid():
            form.save()
            return redirect('lista_ventas')
    else:
        form = DetalleVentaForm(instance=detalles)
    return render(request, 'editar_detalle_venta.html', {'form': form, 'detalles': detalles})


def crear_detalle_venta(request):
    if request.method == 'POST':
        form = DetalleVentaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = DetalleVentaForm()
    return render(request, 'crear_detalle_venta.html', {'form': form})

def eliminar_detalle_venta(request, pk):
    detalles = get_object_or_404(detalles, pk=pk)
    if request.method == 'POST':
        detalles.delete()
        return redirect('lista_detalles_venta')
    return render(request, 'eliminar_detalles_venta.html', {'detalles': detalles})

