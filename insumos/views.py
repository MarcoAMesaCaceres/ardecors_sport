from django.shortcuts import render, get_object_or_404, redirect
from .models import Insumos
from .forms import InsumosForm
from django.db.models import Q
from django.contrib import messages
from django.core.exceptions import ValidationError
from proveedores.models import  Proveedor

def lista_insumos(request):
    insumos = Insumos.objects.all()
    return render(request, 'lista_insumos.html', {'insumos': insumos})


def crear_insumos(request):
    if request.method == 'POST':
        form = InsumosForm(request.POST, request.FILES)
        if form.is_valid():
            insumos = form.save()
            return redirect('lista_insumos')
    else:
        form = InsumosForm()
    return render(request, 'crear_insumos.html', {'form': form})
def editar_insumos(request, pk):
    insumos = get_object_or_404(Insumos, pk=pk)
    if request.method == 'POST':
        form = InsumosForm(request.POST, instance=insumos)
        if form.is_valid():
            form.save()
            messages.success(request, 'El insumo ha sido actualizado exitosamente.')
            return redirect('lista_insumos')
        else:
            messages.error(request, 'Ha ocurrido un error al actualizar el insumo. Por favor, revise los campos.')
    else:
        form = InsumosForm(instance=insumos)
    return render(request, 'editar_insumos.html', {'form': form, 'insumos': insumos})

def eliminar_insumos(request, pk):
    insumos = get_object_or_404(Insumos, pk=pk)
    if request.method == 'POST':
        try:
            insumos.delete()
            messages.success(request, 'El insumo ha sido eliminado exitosamente.')
            return redirect('lista_insumos')
        except ValidationError as e:
            messages.error(request, str(e))
            return redirect('lista_insumos')
    return render(request, 'eliminar_insumos.html', {'insumos': insumos})