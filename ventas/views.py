from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import Venta
from .forms import VentaForm, VentaSearchForm
from django.db.models import Q
from django.core.paginator import Paginator
from django.forms import inlineformset_factory
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from io import BytesIO
import openpyxl
from openpyxl.utils import get_column_letter
from django.http import FileResponse
from reportlab.lib.pagesizes import letter
from django.contrib import messages
from django.core.exceptions import ValidationError

def lista_ventas(request):
    ventas = Venta.objects.all()
    form = VentaSearchForm(request.GET)
    
    if form.is_valid():
        form = VentaSearchForm(request.GET)
    ventas = Venta.objects.all()

    if form.is_valid():
        cliente = form.cleaned_data.get('cliente')
        fecha_inicio = form.cleaned_data.get('fecha_inicio')
        fecha_fin = form.cleaned_data.get('fecha_fin')
        total_min = form.cleaned_data.get('total_min')
        total_max = form.cleaned_data.get('total_max')

        if cliente:
            ventas = ventas.filter(cliente__icontains=cliente)
        if fecha_inicio:
            ventas = ventas.filter(fecha__gte=fecha_inicio)
        if fecha_fin:
            ventas = ventas.filter(fecha__lte=fecha_fin)
        if total_min:
            ventas = ventas.filter(total__gte=total_min)
        if total_max:
            ventas = ventas.filter(total__lte=total_max)
    
    return render(request, 'lista_ventas.html', {'ventas': ventas, 'form': form})

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
def exportar_excel(request):
    ventas = Venta.objects.all()
    
    # Crear libro y hoja de Excel
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = 'Ventas'

    # Agregar encabezados
    headers = ['ID', 'Fecha', 'Cliente', 'Producto', 'Cantidad', 'Precio Unitario', 'Total']
    for col_num, header in enumerate(headers, 1):
        col_letter = get_column_letter(col_num)
        ws[f'{col_letter}1'] = header

    # Agregar filas de ventas
    for row_num, venta in enumerate(ventas, 2):
        ws[f'A{row_num}'] = venta.id
        ws[f'B{row_num}'] = venta.fecha.strftime('%d/%m/%Y')
        ws[f'C{row_num}'] = venta.cliente
        ws[f'D{row_num}'] = venta.producto.nombre if venta.producto else 'No especificado'
        ws[f'E{row_num}'] = venta.cantidad
        ws[f'F{row_num}'] = venta.precio_unitario
        ws[f'G{row_num}'] = venta.total

    # Crear respuesta HTTP para descargar el archivo
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    )
    response['Content-Disposition'] = 'attachment; filename=ventas.xlsx'
    wb.save(response)
    return response

def exportar_pdf(request):
    # Crear un buffer de bytes para el PDF
    buffer = BytesIO()

    # Crear el documento PDF
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []

    # Obtener los datos de las ventas
    ventas = Venta.objects.all()

    # Crear los datos para la tabla
    data = [['ID', 'Cliente', 'Fecha', 'Total']]  # Encabezados
    for venta in ventas:
        data.append([str(venta.id), venta.cliente, str(venta.fecha), str(venta.total)])

    # Crear la tabla
    table = Table(data)
    
    # Estilo de la tabla
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('TOPPADDING', (0, 1), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])
    table.setStyle(style)

    # Agregar la tabla al documento
    elements.append(table)

    # Construir el PDF
    doc.build(elements)

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='ventas.pdf')





