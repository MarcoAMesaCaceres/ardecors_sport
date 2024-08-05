from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import RegistroForm
from django.http import HttpResponse
import os
from datetime import datetime
from django.conf import settings

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
def crear_articles(request):
    return render(request, 'crear_articles.html')
def lista_articles(request):
    return render(request, 'lista_articles.html')
def editar_articles(request):
    return render(request, 'editar_articles.html')
def eliminar_articles(request):
    return render(request, 'eliminar_articles.html')
def base_articles(request):
    return render(request, 'base_articles.html')

def base_tareas(request):
    return render(request, 'base_tareas.html')
def crear_tareas(request):
    return render(request, 'crear_tareas.html')
def lista_tareas(request):
    return render(request, 'lista_tareas.html')
def editar_tareas(request):
    return render(request, 'editar_tareas.html')
def eliminar_tareas(request):
    return render(request, 'eliminar_tareas.html')

def base_compras(request):
    return render(request, 'base_compras.html')
def crear_compras(request):
    return render(request, 'crear_compras.html')
def lista_compras(request):
    return render(request, 'lista_compras.html')
def editar_compras(request):
    return render(request, 'editar_compras.html')
def eliminar_compras(request):
    return render(request, 'eliminar_compras.html')

def base_detalle_compra(request):
    return render(request, 'base_detalle_compra.html')
def crear_detalle_compra(request):
    return render(request, 'crear_detalle_compra.html')
def lista_detalles_compra(request):
    return render(request, 'lista_detalle_compra.html')
def editar_detalle_compra(request):
    return render(request, 'editar_detalles_compra.html')
def eliminar_detalle_compra(request):
    return render(request, 'eliminar_detalle_compra.html')

def base_usuario(request):
    return render(request, 'base_usuario.html')
def crear_usuario(request):
    return render(request, 'crear_usuario.html')
def lista_usuarios(request):
    return render(request, 'lista_usuarios.html')
def editar_usuario(request):
    return render(request, 'editar_usuario.html')
def eliminar_usuario(request):
    return render(request, 'eliminar_usuario.html')

def base_venta(request):
    return render(request, 'base_venta.html')
def crear_venta(request):
    return render(request, 'crear_venta.html')
def lista_ventas(request):
    return render(request, 'lista_ventas.html')
def editar_venta(request):
    return render(request, 'editar_venta.html')
def eliminar_venta(request):
    return render(request, 'eliminar_venta.html')

def base_detalle_venta(request):
    return render(request, 'base_detalle_venta.html')
def crear_detalle_venta(request):
    return render(request, 'crear_detalle_venta.html')
def lista_detalles_venta(request):
    return render(request, 'lista_detalles_venta.html')
def editar_detalle_venta(request):
    return render(request, 'editar_detalle_venta.html')
def eliminar_detalle_venta(request):
    return render(request, 'eliminar_detalle_venta.html')

def base_proveedor(request):
    return render(request, 'base_proveedor.html')
def crear_proveedor(request):
    return render(request, 'crear_proveedor.html')
def lista_proveedores(request):
    return render(request, 'lista_proveedores.html')
def editar_proveedor(request):
    return render(request, 'editar_proveedor.html')
def eliminar_proveedor(request):
    return render(request, 'eliminar_proveedor.html')

def logout_view(request):
    logout(request)
    return redirect('ardecors')

def backup_databases(request):
    return render(request, 'backup_databases.html')

def backup_database_view(request):
    backup_dir = os.path.join(settings.BASE_DIR, 'backups')
    os.makedirs(backup_dir, exist_ok=True)
    
    backup_file = os.path.join(
        backup_dir, f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.sql"
    )
    
    db_name = settings.DATABASES['default']['NAME']
    db_user = settings.DATABASES['default']['USER']
    db_password = settings.DATABASES['default']['PASSWORD']
    db_host = settings.DATABASES['default']['HOST']
    db_port = settings.DATABASES['default']['PORT']
    
    dump_command = (
        f"mysqldump --user={db_user} --password={db_password} --host={db_host} --port={db_port} {db_name} > {backup_file}"
    )
    
    os.system(dump_command)
    
    success_message = f'Respaldo creado exitosamente en {backup_file}'
    
    # Render the success message on the 'backup databases' page
    return render(request, 'backup_databases.html', {'message': success_message})