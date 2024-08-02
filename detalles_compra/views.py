from django.shortcuts import render, get_object_or_404, redirect
from .forms import DetalleCompraForm
from .models import DetalleCompra

def lista_detalles_compra(request):
    detalles = DetalleCompra.objects.all()
    return render(request, 'lista_detalles_compra.html', {'detalles': detalles})

def crear_detalle_compra(request):
    if request.method == 'POST':
        form = DetalleCompraForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = DetalleCompraForm()
    return render(request, 'crear_detalle_compra.html', {'form': form})

def editar_detalle_compra(request):
    if request.method == 'POST':
        form = DetalleCompraForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = DetalleCompraForm()
    return render(request, 'crear_detalle_compra.html', {'form': form})

def eliminar_detalle_compra(request, pk):
    detalle = get_object_or_404(DetalleCompra, pk=pk)
    if request.method == 'POST':
        detalle.delete()
        return redirect('lista_detalles_compra')
    return render(request, 'eliminar_detalles_compra.html', {'detalle': detalle})