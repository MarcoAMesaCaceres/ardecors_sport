from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .forms import ClientesForm
from .models import Clientes
from django.db.models import Q

def lista_clientes(request):
    id_query = request.GET.get('id', '')
    nombre_query = request.GET.get('nombre', '')
    telefono_query = request.GET.get('telefono', '')
    email_query = request.GET.get('email', '')
    direccion_query = request.GET.get('direccion', '')

    clientes = Clientes.objects.all()

    if id_query:
        clientes = clientes.filter(id=id_query)
    if nombre_query:
        clientes = clientes.filter(nombre__icontains=nombre_query)
    if telefono_query:
        clientes = clientes.filter(telefono__icontains=telefono_query)
    if email_query:
        clientes = clientes.filter(email__icontains=email_query)
    if direccion_query:
        clientes = clientes.filter(direccion__icontains=direccion_query)

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
    
    # Verificar si el cliente tiene ventas asociadas
    if cliente.tiene_ventas():
        messages.error(request, "No se puede eliminar el cliente porque tiene ventas asociadas.")
        return redirect('lista_clientes')
        
    if request.method == 'POST':
        try:
            cliente.delete()
            messages.success(request, "Cliente eliminado exitosamente.")
        except Exception as e:
            messages.error(request, "Error al eliminar el cliente.")
        return redirect('lista_clientes')
    
    return render(request, 'eliminar_clientes.html', {'cliente': cliente})