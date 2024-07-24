from django.shortcuts import render, get_object_or_404
from .models import DetalleVenta
from .forms import DetalleVentaForm

def lista_detalles_venta(request):
    detalles = DetalleVenta.objects.all()
    return render(request, 'detalles_venta/lista_detalles_venta.html', {'detalles': detalles})

def detalle_detalle_venta(request, detalle_id):
    detalle = get_object_or_404(DetalleVenta, id=detalle_id)
    return render(request, 'detalles_venta/detalle_detalle_venta.html', {'detalle': detalle})

def crear_detalle_venta(request):
    if request.method == 'POST':
        form = DetalleVentaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = DetalleVentaForm()
    return render(request, 'detalles_venta/crear_detalle_venta.html', {'form': form})
