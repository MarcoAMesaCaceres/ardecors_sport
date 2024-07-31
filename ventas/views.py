from django.shortcuts import get_object_or_404, redirect, render
from .models import Venta
from .forms import VentaForm

def lista_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'lista_ventas.html', {'ventas': ventas})

def detalle_venta(request, venta_id):
    venta = get_object_or_404(Venta, id=venta_id)
    return render(request, 'detalle_venta.html', {'venta': venta})

def crear_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = VentaForm()
    return render(request, 'crear_venta.html', {'form': form})

def eliminar_venta(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        venta.delete()
        return redirect('lista_ventas')
    return render(request, 'eliminar_venta.html', {'venta': venta})

