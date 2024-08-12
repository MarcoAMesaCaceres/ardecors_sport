from django.shortcuts import get_object_or_404, redirect, render
from .models import Venta
from .forms import VentaForm
import io
from django.http import FileResponse
from django.template.loader import get_template
from xhtml2pdf import pisa



def detalle_venta(request, venta_id):
    venta = get_object_or_404(Venta, pk=venta_id)
    return render(request, 'detalle_venta.html', {'venta': venta})

def lista_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'lista_ventas.html', {'ventas': ventas})

def editar_venta(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        form = VentaForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            return redirect('lista_ventas')
    else:
        form = VentaForm(instance=venta)
    return render(request, 'editar_venta.html', {'form': form, 'venta': venta})


def crear_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = VentaForm()
    return render(request, 'crear_venta.html', {'form': form})

def eliminar_venta(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        venta.delete()
        return redirect('lista_ventas')
    return render(request, 'eliminar_venta.html', {'venta': venta})

def exportar_pdf(request):
    ventas = Venta.objects.all()
    template = get_template('ventas_pdf.html')
    context = {'ventas': ventas}
    html = template.render(context)
    result = io.BytesIO()
    pisa.pisaDocument(io.BytesIO(html.encode("UTF-8")), result)
    return FileResponse(result, as_attachment=True, filename='ventas.pdf')


