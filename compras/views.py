from django.shortcuts import get_object_or_404, redirect, render
from .models import Compras
from .forms import ComprasForm, ComprasSearchForm
from django.db.models import Q

# Exportar pdf, excel
from django.http import HttpResponse
from io import BytesIO
import openpyxl
from openpyxl.utils import get_column_letter
from django.http import FileResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle


def lista_compras(request):
    compras = Compras.objects.all()
    form = ComprasSearchForm(request.GET)
    
    if form.is_valid():
        search_query = form.cleaned_data.get('search_query')
        min_total = form.cleaned_data.get('min_total')
        max_total = form.cleaned_data.get('max_total')
        fecha_inicio = form.cleaned_data.get('fecha_inicio')
        fecha_fin = form.cleaned_data.get('fecha_fin')
        
        if search_query:
            compras = compras.filter(
                Q(proveedor__nombre__icontains=search_query) | 
                Q(producto__icontains=search_query)
            )
        
        if min_total:
            compras = compras.filter(total__gte=min_total)
        
        if max_total:
            compras = compras.filter(total__lte=max_total)
        
        if fecha_inicio:
            compras = compras.filter(fecha__gte=fecha_inicio)
        
        if fecha_fin:
            compras = compras.filter(fecha__lte=fecha_fin)
    
    return render(request, 'lista_compras.html', {'compras': compras, 'form': form})

# ... (resto de las vistas)
# compras/views.py

def crear_compras(request):
    if request.method == 'POST':
        form = ComprasForm(request.POST)
        if form.is_valid():
            compra = form.save()
            return redirect('lista_detalles_compra', compra_id=compra.id)
    else:
        form = ComprasForm()
    return render(request, 'crear_compras.html', {'form': form})

def editar_compras(request, pk):
    compra = get_object_or_404(Compras, pk=pk)
    if request.method == 'POST':
        form = ComprasForm(request.POST, instance=compra)
        if form.is_valid():
            form.save()
            return redirect('lista_compras')
    else:
        form = ComprasForm(instance=compra)
    return render(request, 'editar_compras.html', {'form': form, 'compra': compra})

def eliminar_compras(request, pk):
    compra = get_object_or_404(Compras, pk=pk)  # Cambiado de 'compras' a 'Compras'
    if request.method == 'POST':
        compra.delete()
        return redirect('lista_compras')  # Cambiado aquí
    return render(request, 'eliminar_compras.html', {'compra': compra})

def exportar_excel(request):
    compras = Compras.objects.all()
    
    # Crear libro y hoja de Excel
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = 'Compras'

    # Agregar encabezados
    headers = ['ID', 'Fecha', 'Proveedor', 'Producto', 'Cantidad', 'Precio Unitario', 'Total']
    for col_num, header in enumerate(headers, 1):
        col_letter = get_column_letter(col_num)
        ws[f'{col_letter}1'] = header

    # Agregar filas de ventas
    for row_num, venta in enumerate(compras, 2):
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
    compras = Compras.objects.all()

    # Crear los datos para la tabla
    data = [['ID', 'proveedor', 'Fecha', 'Total']]  # Encabezados
    for venta in compras:
        data.append([str(compras.id), compras.proveedor, str(compras.fecha), str(compras.total)])

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
    return FileResponse(buffer, as_attachment=True, filename='compras.pdf')

