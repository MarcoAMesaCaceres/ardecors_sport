from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, ContactoForm, ProductoForm, LoginForm
from .models import Producto, Contacto

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
            form.save()
            return redirect('ardecors')
    else:
        form = ContactoForm()
    return render(request, 'contacto.html', {'form': form})

def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('admin_dashboard')
            else:
                form.add_error(None, 'Credenciales inválidas')
    else:
        form = LoginForm()
    return render(request, 'iniciar_sesion.html', {'form': form})

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('ardecors')
    else:
        form = RegistroForm()
    return render(request, 'iniciar_sesion.html', {'form': form})

@login_required
def admin_dashboard(request):
    return render(request, 'admin_dasboard.html')

@login_required
def configuraciones(request):
    return render(request, 'configuraciones.html')

@login_required
def proveedores(request):
    return render(request, 'proveedores.html')

@login_required
def ordenes_compras(request):
    return render(request, 'ordenes_compras.html')

@login_required
def detalles_compra(request):
    return render(request, 'detalles_compra.html')

@login_required
def detalles_venta(request):
    return render(request, 'detalles_venta.html')

@login_required
def usuarios(request):
    return render(request, 'usuarios.html')

@login_required
def ventas(request):
    return render(request, 'ventas.html')

def logout_view(request):
    logout(request)
    return redirect('ardecors')
@login_required
def ver_carrito(request):
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    items = carrito.items.all()
    total = sum(item.producto.precio * item.cantidad for item in items)
    return render(request, 'carrito.html', {'items': items, 'total': total})

@login_required
def pagar(request):
    # Aquí iría la lógica para procesar el pago
    return render(request, 'pagar.html')

def logout_view(request):
    logout(request)
    return redirect('ardecors')