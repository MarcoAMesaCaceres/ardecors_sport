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
            return redirect('lista_detalles_compra')
    else:
        form = DetalleCompraForm()
    return render(request, 'crear_dettalle_compra.html', {'form': form})


def editar_detalle_compra(request, pk):
    detalles = get_object_or_404(detalles, pk=pk)
    if request.method == 'POST':
        form = DetalleCompraForm(request.POST, instance=detalles)
        if form.is_valid():
            form.save()
            return redirect('lista_compras')
    else:
        form = DetalleCompraForm(instance=detalles)
    return render(request, 'editar_compras.html', {'form': form, 'detalles': detalles})

def eliminar_detalle_compra(request, pk):
    detalles = get_object_or_404(detalles, pk=pk)
    if request.method == 'POST':
        detalles.delete()
        return redirect('lista_detalles_compra.html', {'detalles': detalles})