from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
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
    # Crear un buffer de bytes para el PDF
    buffer = BytesIO()

    # Crear el documento PDF
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []
    
    # Agregar el logo con la ruta absoluta
    logo_path = os.path.join(settings.BASE_DIR, 'static', 'Image', 'ardecorslogo.png')
    logo = Image(logo_path, width=2*inch, height=2*inch)
    elements.append(logo)
    elements.append(Spacer(1, 12))
    
    # Agregar el título
    styles = getSampleStyleSheet()
    elements.append(Paragraph("Empresa de balones Ardecors", styles['Title']))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph("Lista de Ventas", styles['Heading1']))
    elements.append(Spacer(1, 12))

    # Obtener los datos de las ventas
    ventas = Venta.objects.all()

    # Crear los datos para la tabla en el orden correcto
    data = [['ID', 'Fecha', 'Cliente', 'Artículo', 'Total']]  # Encabezados
    for venta in ventas:
        data.append([str(venta.id), str(venta.fecha), venta.cliente, venta.articulo, str(venta.total)])

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
@require_GET
def exportar_excel(request):
    # Crea un archivo de Excel en memoria
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
