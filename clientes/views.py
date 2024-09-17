from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import clientes
from .forms import ClientesForm

def lista_clientes(request):
    clientes = clientes.objects.all()
    return render(request, 'lista_clientes.html', {'clientes': clientes})

def editar_clientes(request, pk):
    clientes = get_object_or_404(clientes, pk=pk)
    if request.method == 'POST':
        form = ClientesForm(request.POST, instance=clientes)
        if form.is_valid():
            form.save()
            messages.success(request, "clientes actualizado exitosamente.")
            return redirect('lista_clientes')
        else:
            messages.error(request, "Error al actualizar clientes. Por favor, revise los datos.")
    else:
        form = ClientesForm(instance=clientes)
    return render(request, 'editar_clientes.html', {'form': form, 'clientes': clientes})

def crear_clientes(request):
    if request.method == 'POST':
        form = ClientesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "clientes creado exitosamente.")
            return redirect('lista_clientes')
        else:
            messages.error(request, "Error al crear clientes. Por favor, revise los datos.")
    else:
        form = ClientesForm()
    return render(request, 'crear_clientes.html', {'form': form})

def eliminar_clientes(request, pk):
    clientes = get_object_or_404(clientes, pk=pk)
    if request.method == 'POST':
        clientes.delete()
        messages.success(request, "clientes eliminado exitosamente.")
        return redirect('lista_clientes')
    return render(request, 'eliminar_clientes.html', {'clientes': clientes})