from django.shortcuts import render, get_object_or_404, redirect
from .models import Configuracion
from .forms import ConfiguracionForm

def lista_configuraciones(request):
    configuraciones = Configuracion.objects.all()
    return render(request, 'lista_configuraciones.html', {'configuraciones': configuraciones})



def crear_configuracion(request):
    if request.method == 'POST':
        form = ConfiguracionForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ConfiguracionForm()
    return render(request, 'crear_configuracion.html', {'form': form})
    
def editar_configuracion(request, pk):
    configuracion = get_object_or_404(Configuracion, pk=pk)
    if request.method == 'POST':
        form = ConfiguracionForm(request.POST, instance=configuracion)
        if form.is_valid():
            form.save()
            return redirect('lista_configuraciones')
    else:
        form = ConfiguracionForm(instance=configuracion)
    return render(request, 'editar_configuracion.html', {'form': form, 'configuracion': configuracion})


def eliminar_configuraciones(request, pk):
    configuracion = get_object_or_404(Configuracion, pk=pk)
    if request.method == 'POST':
        configuracion.delete()
        return redirect('lista_configuraciones')
    return render(request, 'eliminar_configuraciones.html', {'configuracion': configuracion})