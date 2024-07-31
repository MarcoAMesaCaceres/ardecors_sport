from django.shortcuts import get_object_or_404, redirect, render
from .models import Usuario
from .forms import UsuarioForm

def lista_usuarios(request):
    usuario = Usuario.objects.all()
    return render(request, 'lista_usuarios.html', {'usuario': usuario})

def detalle_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    return render(request, 'detalle_usuario.html', {'usuario': usuario})

def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UsuarioForm()
    return render(request, 'crear_usuario.html', {'form': form})

def eliminar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('lista_usuarios')
    return render(request, 'eliminar_usuario.html', {'usuario': usuario})
