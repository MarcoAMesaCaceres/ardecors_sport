from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from reportlab.lib.utils import ImageReader
from .models import Venta
from .forms import VentaForm
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from io import BytesIO
from django.http import FileResponse
from reportlab.lib.pagesizes import letter
from django.contrib import messages
from django.core.exceptions import ValidationError
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Spacer
from django.views.decorators.http import require_GET
from reportlab.lib.units import inch
import xlsxwriter
import io
import os
from django.conf import settings
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.templatetags.static import static
from reportlab.lib.enums import TA_LEFT
from django.db.models import Q
from django.shortcuts import render
from .models import Venta


def lista_ventas(request):
    id_query = request.GET.get('id', '')
    fecha_query = request.GET.get('fecha', '')
    cliente_query = request.GET.get('cliente', '')
    articulo_query = request.GET.get('articulo', '')

    # Filtrado inicial
    ventas = Venta.objects.all().prefetch_related('detalles__articulo')

    # Validación y filtrado por ID
    if id_query and not id_query.isdigit():
        messages.error(request, "Debe colocar un número válido para el ID.")
    else:
        if id_query:
            ventas = ventas.filter(id=id_query)

    # Filtrado por fecha
    if fecha_query:
        ventas = ventas.filter(fecha__date=fecha_query)  # Asegúrate de que `fecha` sea un campo DateTimeField

    # Filtrado por cliente (asumiendo que hay una relación)
    if cliente_query:
        ventas = ventas.filter(cliente__nombre__icontains=cliente_query)

    # Filtrado por artículo
    if articulo_query:
        ventas = ventas.filter(detalles__articulo__nombre__icontains=articulo_query)

    return render(request, 'lista_ventas.html', {'ventas': ventas})

def crear_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            try:
                venta = form.save()
                messages.success(request, 'Venta creada exitosamente.')
                return redirect('crear_detalle_venta', venta_id=venta.id)
            except ValidationError as e:
                for field, errors in e.message_dict.items():
                    for error in errors:
                        form.add_error(field, error)
        
        if form.errors:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = VentaForm()
    return render(request, 'crear_venta.html', {'form': form})

def editar_venta(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        form = VentaForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            messages.success(request, 'Venta actualizada exitosamente.')
            return redirect('lista_ventas')
        else:
            messages.error(request, 'Por favor, corrija los errores en el formulario.')
    else:
        form = VentaForm(instance=venta)
    return render(request, 'editar_venta.html', {'form': form, 'venta': venta})
def crear_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            venta = form.save()
            # Redirigir a la página de crear detalle de venta
            return redirect('crear_detalle_venta', venta_id=venta.id)
    else:
        form = VentaForm()
    return render(request, 'crear_venta.html', {'form': form})

def eliminar_venta(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        venta.delete()
        messages.success(request, 'Venta eliminada exitosamente.')
        return redirect('lista_ventas')
    return render(request, 'eliminar_venta.html', {'venta': venta})

