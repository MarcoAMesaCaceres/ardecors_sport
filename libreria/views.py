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
def logout_view(request):
    logout(request)
    return redirect('ardecors')
