from django.shortcuts import render, get_object_or_404
from django.conf import settings
from .models import ArticuloAyuda
from django.http import FileResponse
import os

def lista_ayuda(request):
    articulos = ArticuloAyuda.objects.all()
    return render(request, 'ayuda/lista_ayuda.html', {'articulos': articulos})

def detalle_ayuda(request, pk):
    articulo = get_object_or_404(ArticuloAyuda, pk=pk)
    return render(request, 'ayuda/detalle_ayuda.html', {'articulo': articulo})

def manual_usuario(request):
    pdf_path = os.path.join('ruta', 'a', 'tu', 'Manual_de_Usuario_Ardecors.pdf')
    return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')

def descargar_manual(request):
    pdf_path = os.path.join(settings.STATICFILES_DIRS[0], 'docs/Manual_de_Usuario_Ardecors.pdf')
    return FileResponse(open(pdf_path, 'rb'), as_attachment=True, content_type='application/pdf')