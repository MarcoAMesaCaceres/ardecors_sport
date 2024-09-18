from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .forms import ClientesForm
from .models import Clientes  # Assume the model name is capitalized

def lista_clientes(request):
    clientes = Clientes.objects.all()
    return render(request, 'lista_clientes.html', {'clientes': clientes})

def editar_clientes(request, pk):
    cliente = get_object_or_404(Clientes, pk=pk)
    if request.method == 'POST':
        form = ClientesForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente actualizado exitosamente.")
            return redirect('lista_clientes')
        else:
            messages.error(request, "Error al actualizar cliente. Por favor, revise los datos.")
    else:
        form = ClientesForm(instance=cliente)
    return render(request, 'editar_clientes.html', {'form': form, 'cliente': cliente})

def crear_clientes(request):
    if request.method == 'POST':
        form = ClientesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente creado exitosamente.')
            return redirect('lista_clientes')  # Redirige a la lista de clientes después de guardar
        else:
            messages.error(request, 'Por favor, corrija los errores a continuación.')
    else:
        form = ClientesForm()

    return render(request, 'crear_clientes.html', {'form': form})

def eliminar_clientes(request, pk):
    cliente = get_object_or_404(Clientes, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        messages.success(request, "Cliente eliminado exitosamente.")
        return redirect('lista_clientes')
    return render(request, 'eliminar_clientes.html', {'cliente': cliente})
