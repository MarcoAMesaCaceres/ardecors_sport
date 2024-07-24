from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistroForm, ContactoForm
from .models import Producto

def ardecors(request):
    return render(request, 'ardecors.html')

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})

def sobre(request):
    return render(request, 'sobre.html')

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            # Procesar el formulario
            return redirect('ardecors')
    else:
        form = ContactoForm()
    return render(request, 'contacto.html', {'form': form})

def iniciar_sesion(request):
    # Implementar lógica de inicio de sesión
    return render(request, 'iniciar_sesion.html')

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('ardecors')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})