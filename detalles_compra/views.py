from django.shortcuts import render, get_object_or_404, redirect
from .forms import DetalleCompraForm
from .models import DetalleCompra
from compras.models import Compras  # Añade esta importación

# Exportar pdf, excel
from django.http import HttpResponse
from io import BytesIO
import openpyxl
from openpyxl.utils import get_column_letter
from django.http import FileResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle




def lista_detalles_compra(request, compra_id=None):
    if compra_id:
        compra = get_object_or_404(Compras, id=compra_id)
        detalles = DetalleCompra.objects.filter(compra_id=compra_id)
    else:
        compra = None
        detalles = DetalleCompra.objects.all()
    return render(request, 'lista_detalles_compra.html', {'detalles': detalles, 'compra': compra})

def crear_detalle_compra(request, compra_id):
    compra = get_object_or_404(Compras, id=compra_id)
    if request.method == 'POST':
        form = DetalleCompraForm(request.POST)
        if form.is_valid():
            detalle = form.save(commit=False)
            detalle.compra = compra
            detalle.save()
            compra.actualizar_total()
            return redirect('lista_detalles_compra', compra_id=compra.id)
    else:
        form = DetalleCompraForm()
    return render(request, 'crear_detalle_compra.html', {'form': form, 'compra': compra})

def editar_detalle_compra(request, pk):
    detalle = get_object_or_404(DetalleCompra, pk=pk)
    if request.method == 'POST':
        form = DetalleCompraForm(request.POST, instance=detalle)
        if form.is_valid():
            detalle = form.save()
            return redirect('lista_detalles_compra', compra_id=detalle.compra.id)
    else:
        form = DetalleCompraForm(instance=detalle)
    return render(request, 'editar_detalle_compra.html', {'form': form, 'detalle': detalle})

def eliminar_detalle_compra(request, pk):
    detalle = get_object_or_404(DetalleCompra, pk=pk)
    if request.method == 'POST':
        compra_id = detalle.compra.id
        detalle.delete()
        return redirect('lista_detalles_compra', compra_id=compra_id)
    return render(request, 'eliminar_detalle_compra.html', {'detalle': detalle})

