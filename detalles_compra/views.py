from django.shortcuts import render, get_object_or_404, redirect
from .forms import DetalleCompraForm
from .models import DetalleCompra
from compras.models import Compras  # Añade esta importación

def lista_detalles_compra(request):
    detalles = DetalleCompra.objects.all()
    return render(request, 'lista_detalles_compra.html', {'detalles': detalles})

def crear_detalle_compra(request, compra_id):
    compra = get_object_or_404(Compras, id=compra_id)
    if request.method == 'POST':
        form = DetalleCompraForm(request.POST)
        if form.is_valid():
            detalle = form.save(commit=False)
            detalle.compra = compra
            detalle.save()
            return redirect('lista_detalles_compra')
    else:
        form = DetalleCompraForm(initial={'compra': compra})
    return render(request, 'crear_detalle_compra.html', {'form': form, 'compra': compra})


def editar_detalle_compra(request, pk):
    detalle = get_object_or_404(DetalleCompra, pk=pk)
    if request.method == 'POST':
        form = DetalleCompraForm(request.POST, instance=detalle)
        if form.is_valid():
            form.save()
            return redirect('lista_detalles_compra')
    else:
        form = DetalleCompraForm(instance=detalle)
    return render(request, 'editar_detalle_compra.html', {'form': form, 'detalle': detalle})

def eliminar_detalle_compra(request, pk):
    detalle = get_object_or_404(DetalleCompra, pk=pk)  # Cambia 'detalles' a 'DetalleCompra'
    if request.method == 'POST':
        detalle.delete()
        return redirect('lista_detalles_compra')  # Elimina '.html' y el diccionario