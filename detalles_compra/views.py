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
    
def exportar_excel(request):
    detalleCompra = DetalleCompra.objects.all()
    
    # Crear libro y hoja de Excel
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = 'detalleCompra'

    # Agregar encabezados
    headers = ['ID', 'Fecha', 'Proveedor', 'Producto', 'Cantidad', 'Precio Unitario', 'Total']
    for col_num, header in enumerate(headers, 1):
        col_letter = get_column_letter(col_num)
        ws[f'{col_letter}1'] = header

    # Agregar filas de ventas
    for row_num, venta in enumerate(detalleCompra, 2):
        ws[f'A{row_num}'] = detalleCompra.id
        ws[f'B{row_num}'] = detalleCompra.fecha.strftime('%d/%m/%Y')
        ws[f'C{row_num}'] = detalleCompra.cliente
        ws[f'D{row_num}'] = detalleCompra.producto.nombre if detalleCompra.producto else 'No especificado'
        ws[f'E{row_num}'] = detalleCompra.cantidad
        ws[f'F{row_num}'] = detalleCompra.precio_unitario
        ws[f'G{row_num}'] = detalleCompra.total

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
    detalleCompra = DetalleCompra.objects.all()

    # Crear los datos para la tabla
    data = [['ID', 'proveedor', 'Fecha', 'Total']]  # Encabezados
    for venta in detalleCompra:
        data.append([str(detalleCompra.id), detalleCompra.proveedor, str(detalleCompra.fecha), str(detalleCompra.total)])

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
    return FileResponse(buffer, as_attachment=True, filename='detalleCompra.pdf')

