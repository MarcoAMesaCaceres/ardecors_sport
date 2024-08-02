from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import RegistroForm
def ardecors(request):
    return render(request, 'ardecors.html')

def productos(request):

    return render(request, 'productos.html', {'productos': productos})

def sobre(request):
    return render(request, 'sobre.html')

def contacto(request):
    return render(request, 'contacto.html', {'contato': contacto})

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
def eliminar_articles(request):
    return render(request, 'eliminar_articles.html')
def base_articles(request):
    return render(request, 'base_articles.html')
def base_configuracion(request):
    return render(request, 'base_configuracion.html')
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
def eliminar_detalles_compra(request):
    return render(request, 'eliminar_detalles_compra.html')
def crear_proveedor(request):
    return render(request, 'crear_proveedor.html')
def lista_proveedores(request):
    return render(request, 'lista_proveedores.html')
def crear_configuracion(request):
    return render(request, 'crear_configuracion.html')
def lista_configuraciones(request):
    return render(request, 'lista_configuraciones.html')
def editar_configuracion(request):
    return render(request, 'editar_configuracion.html')
def eliminar_configuraciones(request):
    return render(request, 'eliminar_configuraciones.html')



def logout_view(request):
    logout(request)
    return redirect('ardecors')
