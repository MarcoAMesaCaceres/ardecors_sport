from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Venta, DetalleVenta
from .forms import DetalleVentaForm
from django.http import JsonResponse

def crear_detalle_venta(request, venta_id):
    venta = get_object_or_404(Venta, id=venta_id)
    if request.method == 'POST':
        form = DetalleVentaForm(request.POST)
        if form.is_valid():
            detalle = form.save(commit=False)
            detalle.venta = venta
            detalle.save()
            messages.success(request, 'Detalle de venta creado exitosamente.')
            return redirect('lista_detalles_venta', venta_id=venta.id)
    else:
        form = DetalleVentaForm()
    return render(request, 'crear_detalle_venta.html', {'form': form, 'venta': venta})

def get_articulo_info(request):
    articulo_id = request.GET.get('articulo_id')
    articulo = get_object_or_404(Article, id=articulo_id)
    return JsonResponse({
        'precio': float(articulo.precio),
        'stock': articulo.stock
    })
def lista_detalles_venta(request, venta_id):
    venta = get_object_or_404(Venta, id=venta_id)
    detalles = DetalleVenta.objects.filter(venta=venta)
    return render(request, 'lista_detalles_venta.html', {'venta': venta, 'detalles': detalles})

def editar_detalle_venta(request, detalle_id):
    detalle = get_object_or_404(DetalleVenta, id=detalle_id)
    if request.method == 'POST':
        form = DetalleVentaForm(request.POST, instance=detalle)
        if form.is_valid():
            form.save()
            messages.success(request, 'Detalle de venta actualizado exitosamente.')
            return redirect('lista_detalles_venta', venta_id=detalle.venta.id)
    else:
        form = DetalleVentaForm(instance=detalle)
    return render(request, 'editar_detalle_venta.html', {'form': form, 'detalle': detalle})

def eliminar_detalle_venta(request, detalle_id):
    detalle = get_object_or_404(DetalleVenta, id=detalle_id)
    venta_id = detalle.venta.id
    if request.method == 'POST':
        detalle.delete()
        messages.success(request, 'Detalle de venta eliminado exitosamente.')
        return redirect('lista_detalles_venta', venta_id=venta_id)
    return render(request, 'eliminar_detalle_venta.html', {'detalle': detalle})