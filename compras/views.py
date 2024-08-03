from django.shortcuts import get_object_or_404, redirect, render
from .models import Compras
from .forms import ComprasForm

def lista_compras(request):
    compras = Compras.objects.all()
    return render(request, 'lista_compras.html', {'compras': compras})

def crear_compras(request):
    if request.method == 'POST':
        form = ComprasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_compras')
    else:
        form = ComprasForm()
    return render(request, 'crear_acompras.html', {'form': form})

def editar_compras(request, pk):
    compras = get_object_or_404(Compras, pk=pk)
    if request.method == 'POST':
        form = ComprasForm(request.POST, instance=compras)
        if form.is_valid():
            form.save()
            return redirect('lista_compras')
    else:
        form = ComprasForm(instance=compras)
    return render(request, 'editar_compras.html', {'form': form, 'compras': compras})

def eliminar_compras(request, pk):
    compras = get_object_or_404(compras, pk=pk)
    if request.method == 'POST':
        compras.delete()
        return redirect('lista_compras.html', {'compras': compras})