from django.shortcuts import render, get_object_or_404, redirect, render
from .models import DetalleVenta,Venta
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


def crear_detalle_venta(request, venta_id):
    venta = get_object_or_404(Venta, id=venta_id)
    if request.method == 'POST':
        form = DetalleVentaForm(request.POST)
        if form.is_valid():
            detalle = form.save(commit=False)
            detalle.venta = venta
            detalle.save()
            # Puedes redirigir a la lista de detalles o a donde prefieras
            return redirect('lista_detalles_venta')
    else:
        form = DetalleVentaForm(initial={'venta': venta})
    return render(request, 'crear_detalle_venta.html', {'form': form, 'venta': venta})

def eliminar_detalle_venta(request, pk):
    detalles = get_object_or_404(detalles, pk=pk)
    if request.method == 'POST':
        detalles.delete()
        return redirect('lista_detalles_venta')
    return render(request, 'eliminar_detalles_venta.html', {'detalles': detalles})

