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
import xlsxwriter
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

def exportar_excel(request):
    # Crear un buffer de bytes para el archivo Excel
    buffer = BytesIO()

    # Crear un nuevo libro de trabajo de Excel y agregar una hoja
    workbook = xlsxwriter.Workbook(buffer)
    worksheet = workbook.add_worksheet()

    # Definir estilos
    titulo_estilo = workbook.add_format({
        'bold': True,
        'font_size': 14,
        'align': 'center',
        'valign': 'vcenter',
        'bg_color': '#4F81BD',
        'font_color': 'white'
    })

    dato_estilo = workbook.add_format({
        'align': 'center',
        'valign': 'vcenter'
    })

    # Escribir los encabezados
    encabezados = ['ID', 'Cliente', 'Fecha', 'Total', 'Artículo']
    for col, encabezado in enumerate(encabezados):
        worksheet.write(0, col, encabezado, titulo_estilo)

    # Obtener los datos de las ventas
    ventas = Venta.objects.all()

    # Escribir los datos en el Excel
    for row, venta in enumerate(ventas, start=1):
        worksheet.write(row, 0, venta.id, dato_estilo)
        worksheet.write(row, 1, venta.cliente, dato_estilo)
        worksheet.write(row, 2, venta.fecha.strftime('%Y-%m-%d'), dato_estilo)
        worksheet.write(row, 3, float(venta.total), dato_estilo)
        worksheet.write(row, 4, venta.articulo.name if venta.articulo else 'N/A', dato_estilo)

    # Ajustar el ancho de las columnas
    for i, _ in enumerate(encabezados):
        worksheet.set_column(i, i, 15)

    # Cerrar el libro de trabajo
    workbook.close()

    # Preparar la respuesta HTTP
    buffer.seek(0)
    response = HttpResponse(buffer.getvalue(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=ventas.xlsx'

    return response
