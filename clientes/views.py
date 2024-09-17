from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .forms import ClientesForm
from .models import clientes  # Importación corregida

def lista_clientes(request):
    clientes_list = clientes.objects.all()  # Nombre de variable cambiado para evitar conflicto
    return render(request, 'lista_clientes.html', {'clientes': clientes_list})

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

def crear_cliente(request):
    if request.method == 'POST':
        form = ClientesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes_list')  # Redirige a una lista de clientes después de guardar
    else:
        form = ClientesForm()

    return render(request, 'crear_cliente.html', {'form': form})

def eliminar_clientes(request, pk):
    clientes = get_object_or_404(clientes, pk=pk)
    if request.method == 'POST':
        clientes.delete()
        messages.success(request, "clientes eliminado exitosamente.")
        return redirect('lista_clientes')
    return render(request, 'eliminar_clientes.html', {'clientes': clientes})