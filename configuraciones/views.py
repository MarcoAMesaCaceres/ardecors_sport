from django.shortcuts import render, get_object_or_404, redirect
from .models import Configuracion
from .forms import ConfiguracionForm

def lista_configuraciones(request):
    configuraciones = Configuracion.objects.all()
    return render(request, 'lista_configuraciones.html', {'configuraciones': configuraciones})

def detalle_configuracion(request, config_id):
    configuracion = get_object_or_404(Configuracion, id=config_id)
    return render(request, 'detalle_configuracion.html', {'configuracion': configuracion})

def crear_configuracion(request):
    if request.method == 'POST':
        form = ConfiguracionForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ConfiguracionForm()
    return render(request, 'crear_configuracion.html', {'form': form})

def eliminar_configuracion(request, pk):
    configuracion = get_object_or_404(Configuracion, pk=pk)
    if request.method == 'POST':
        configuracion.delete()
        return redirect('lista_configuraciones')
    return render(request, 'confirmar_eliminacion.html', {'configuracion': configuracion})