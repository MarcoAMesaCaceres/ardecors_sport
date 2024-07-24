from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Producto, Usuario, Producto, Material, Compra, Venta, TipoDePago, TipoDeProducto
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from .forms import UsuarioForm, ProductoForm, MaterialForm, CompraForm, VentaForm
from django.urls import reverse 

# CRUD para Usuario
def usuario_list(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuario/usuario_list.html', {'usuarios': usuarios})

def usuario_detail(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    return render(request, 'usuario_detail.html', {'usuario': usuario})

def usuario_create(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            # Aquí podrías redirigir a usuario_list o a cualquier otra página
    else:
        form = UsuarioForm()
    
    return render(request, 'usuario/usuario_form.html', {'form': form})

def usuario_update(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuario_list')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuario_form.html', {'form': form})

def usuario_delete(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('usuario_list')
    return render(request, 'usuario_confirm_delete.html', {'usuario': usuario})

# Repite el mismo patrón para Producto, Material, TipoDePago, Compra y Venta
# ...
def ardecors(request):
    return render(request, 'ardecors.html')

def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')  
        else:
            return render(request, 'iniciar_sesion.html', {'error': 'Usuario o contraseña incorrectos'})
    return render(request, 'iniciar_sesion.html')

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('iniciar_sesion')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})

def contacto(request):
    return render(request, 'contacto.html')

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})

def crear(request):
    #formulario = ArdecorForm(request.POST or None)
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        Producto.objects.create(nombre=nombre, descripcion=descripcion, precio=precio)
        return redirect('#')
    return render(request, 'crear.html')

def editar(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.nombre = request.POST['nombre']
        producto.descripcion = request.POST['descripcion']
        producto.precio = request.POST['precio']
        producto.save()
        return redirect('#')
    return render(request, 'editar.html', {'producto': producto})

def index(request):
    productos = Producto.objects.all()
    return render(request, 'index.html', {'productos': productos})

def eliminar(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('#')
    return redirect('#')

def sobre(request):
    return render(request, 'sobre.html')

def msobre(request):
    return redirect('sobre')

def cerrar_sesion(request):
    logout(request)
    return redirect('iniciar_sesion')

def custom_logout(request):
    if request.method == 'GET':
        logout(request)
        return redirect('login')
    


def admin_dashboard(request):
    context = {
        'usuario_count': Usuario.objects.count(),
        'productos_count': Producto.objects.count(),
        'materiales_count': Material.objects.count(),
        'compras_count': Compra.objects.count(),
        'ventas_count': Venta.objects.count(),
    }
    return render(request, 'admin_dashboard.html', context)
