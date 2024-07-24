from django.shortcuts import render, get_object_or_404
from .models import Venta
from .forms import VentaForm

def lista_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'ventas/lista_ventas.html', {'ventas': ventas})

def detalle_venta(request, venta_id):
    venta = get_object_or_404(Venta, id=venta_id)
    return render(request, 'ventas/detalle_venta.html', {'venta': venta})

def crear_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = VentaForm()
    return render(request, 'ventas/crear_venta.html', {'form': form})
