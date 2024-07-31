from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import RegistroForm, ContactoForm
from .models import Producto, Carrito, ItemCarrito # Asegúrate de importar los modelos necesarios

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
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('admin_dashboard'))
        else:
            return render(request, 'iniciar_sesion.html', {'error': 'Credenciales incorrectas'})
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
    return render(request, 'iniciar_sesion.html', {'form': form})

@login_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')
@login_required
def crear_usuario(request):
    return render(request, 'crear_usuario.html')
def lista_usuarios(request):
    return render(request, 'lista_usuarios.html')

def crear_articles(request):
    return render(request, 'crear_articles.html')
def lista_articles(request):
    return render(request, 'lista_articles.html')

def crear_venta(request):
    return render(request, 'crear_venta.html')

def lista_ventas(request):
    return render(request, 'lista_ventas.html')

def crear_detalle_venta(request):
    return render(request, 'crear_detalle_venta.html')
def lista_detalles_venta(request):
    return render(request, 'lista_detalles_venta.html')

def crear_orden_compra(request):
    return render(request, 'crear_orden_compra.html')
def lista_ordenes_compra(request):
    return render(request, 'lista_ordenes_compra.html')

def crear_detalle_compra(request):
    return render(request, 'crear_detalle_compra.html')
def lista_detalles_compra(request):
    return render(request, 'lista_detalles_compra.html')

def crear_proveedor(request):
    return render(request, 'crear_proveedor.html')
def lista_proveedores(request):
    return render(request, 'lista_proveedores.html')



def crear_configuracion(request):
    return render(request, 'crear_configuracion.html')
def lista_configuraciones(request):
    return render(request, 'lista_configuraciones.html')

@login_required
def ver_carrito(request):
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    items = carrito.items.all()
    total = sum(item.cantidad * item.producto.precio for item in items)
    return render(request, 'carrito.html', {'items': items, 'total': total})

@login_required
def pagar(request):
    # Aquí iría la lógica para procesar el pago
    return render(request, 'pagar.html')

@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    item, created = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
    item.cantidad += 1
    item.save()
    return redirect('ver_carrito')

def logout_view(request):
    logout(request)
    return redirect('ardecors')
