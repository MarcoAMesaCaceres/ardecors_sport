from django.shortcuts import get_object_or_404, redirect, render
from .models import Compras
from .forms import ComprasForm, ComprasSearchForm
from django.db.models import Q
from django.template.loader import get_template

# Exportar pdf, excel
from django.http import HttpResponse
from io import BytesIO
import openpyxl
from openpyxl.utils import get_column_letter
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch



def lista_compras(request):
    compras = Compras.objects.all()
    form = ComprasSearchForm(request.GET)
    
    if form.is_valid():
        search_query = form.cleaned_data.get('search_query')
        fecha_inicio = form.cleaned_data.get('fecha_inicio')
        fecha_fin = form.cleaned_data.get('fecha_fin')
        
        if search_query:
            compras = compras.filter(
                Q(proveedor__nombre__icontains=search_query) | 
                Q(producto__icontains=search_query)
            )
        
        if fecha_inicio:
            compras = compras.filter(fecha__gte=fecha_inicio)
        
        if fecha_fin:
            compras = compras.filter(fecha__lte=fecha_fin)
    
    return render(request, 'lista_compras.html', {'compras': compras, 'form': form})

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

    # Agregar filas de compras
    for row_num, compra in enumerate(compras, 2):
        ws[f'A{row_num}'] = compra.id
        ws[f'B{row_num}'] = compra.fecha.strftime('%d/%m/%Y')
        ws[f'C{row_num}'] = compra.proveedor.nombre if compra.proveedor else 'No especificado'
        ws[f'D{row_num}'] = compra.producto
        ws[f'E{row_num}'] = 'No aplica'  # Asume que no se tiene cantidad en el modelo
        ws[f'F{row_num}'] = 'No aplica'  # Asume que no se tiene precio_unitario en el modelo
        ws[f'G{row_num}'] = compra.total

    # Crear respuesta HTTP para descargar el archivo
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    )
    response['Content-Disposition'] = 'attachment; filename=compras.xlsx'

def exportar_pdf_compras(request):
    # Crear un buffer en memoria
    buffer = BytesIO()

    # Crear un documento PDF con el buffer
    doc = SimpleDocTemplate(buffer, pagesize=letter)

    # Consulta los datos de compras
    compras = Compras.objects.all()

    # Preparar los datos para la tabla
    data = []
    data.append(['Fecha', 'Proveedor', 'Producto', 'Detalle'])  # Encabezado
    for compra in compras:
        data.append([
            str(compra.fecha),
            compra.proveedor if compra.proveedor else 'N/A',
            compra.producto if compra.producto else 'N/A',
            str(compra)
        ])

    # Crear una tabla
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    # Construir el documento PDF
    doc.build([table])

    # Obtener el valor del buffer y cerrarlo
    pdf = buffer.getvalue()
    buffer.close()

    # Crear una respuesta HTTP con el PDF
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="compras.pdf"'
    return response