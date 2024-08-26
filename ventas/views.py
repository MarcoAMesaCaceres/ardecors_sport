from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from reportlab.lib.utils import ImageReader
from .models import Venta
from .forms import VentaForm, VentaSearchForm
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

def exportar_pdf(request):
    styles = getSampleStyleSheet()
    # Crear un buffer de bytes para el PDF
    buffer = BytesIO()

    # Definir una función para agregar el pie de página
    def agregar_pie_pagina(canvas, doc):
        canvas.saveState()
        canvas.setFont('Helvetica', 10)
        canvas.drawString(inch, 0.75 * inch, "Fabrica de Balones,  Ardecors Sport, Monguí(Boyacá), Guillermo Ladino, No celular 3124933921.")
        canvas.restoreState()

    doc = SimpleDocTemplate(buffer, pagesize=letter, 
                            rightMargin=inch, leftMargin=inch, 
                            topMargin=inch, bottomMargin=inch)
    doc.build_on_single_page = False
    elements = []

    # Ruta del logo
    logo_path = os.path.join(settings.STATICFILES_DIRS[0], 'D:/ardecors_django/sistema/ventas/static/Image/logo.png')

    # Crear la tabla para el logo y el título
    if os.path.exists(logo_path):
        logo = Image(logo_path, width=1.0*inch, height=1.0*inch)
    else:
        logo = Paragraph("Ardecors - Sport", styles['Normal'])
        
    title_style = styles['Title']
    title_style.alignment = TA_LEFT
    
    title = Paragraph("Ardecors Sport", styles['Title'])
    
    title_spacer = Spacer(1, 12)
    
    subtitle = Paragraph("Lista de Ventas", styles['Heading1'])
    

    header_table = Table([[logo, title]], colWidths=[2 * inch, 4 * inch])
    header_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (0, 0), 'TOP'),
        ('VALIGN', (1, 0), (1, 0), 'MIDDLE'),
        ('ALIGN', (1, 0), (1, 0), 'CENTER')
    ]))

    elements.append(header_table)
    elements.append(title_spacer)
    elements.append(subtitle)
    elements.append(Spacer(1, 12))

    # Obtener los datos de las ventas
    ventas = Venta.objects.all()
    data = [['ID', 'Fecha', 'Cliente', 'Artículo', 'Total']]  # Encabezados
    for venta in ventas:
        data.append([str(venta.id), str(venta.fecha), venta.cliente, venta.articulo, str(venta.total)])

    table = Table(data)
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('TOPPADDING', (0, 1), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])
    table.setStyle(style)

    elements.append(table)

    # Construir el PDF con el pie de página
    doc.build(elements, onFirstPage=agregar_pie_pagina, onLaterPages=agregar_pie_pagina)

    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='ventas.pdf')


@require_GET
def exportar_excel(request):
    # Crea un archivo de Excel en memoria jajajajaj
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()

    # Agrega el encabezado
    bold = workbook.add_format({'bold': True})
    worksheet.merge_range('A1:G1', 'Empresa de balones Ardecors', bold)

    # Agrega los títulos de las columnas
    columns = ['ID', 'Fecha', 'Cliente', 'Producto', 'Cantidad', 'Precio Unitario', 'Total']
    for col, title in enumerate(columns):
        worksheet.write(1, col, title, bold)

    # Obtén los datos de tus ventas
    ventas = Venta.objects.all()  # Ajusta esto según tu modelo y consulta

    # Escribe los datos
    for row, venta in enumerate(ventas, start=2):
        worksheet.write(row, 0, venta.id)
        worksheet.write(row, 1, venta.fecha.strftime('%d/%m/%Y'))
        worksheet.write(row, 2, venta.cliente)
        worksheet.write(row, 3, venta.producto.nombre if venta.producto else 'No especificado')
        worksheet.write(row, 4, venta.cantidad)
        worksheet.write(row, 5, venta.precio_unitario)
        worksheet.write(row, 6, venta.total)

    workbook.close()

    # Prepara la respuesta
    output.seek(0)
    response = HttpResponse(output.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="ventas_ardecors.xlsx"'
    
    return response
