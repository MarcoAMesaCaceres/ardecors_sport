from django.shortcuts import render, get_object_or_404, redirect
from .models import Tarea
from .forms import TareaForm

def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'lista_tareas.html', {'tareas': tareas})



def crear_tareas(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')
    else:
        form = TareaForm()
    return render(request, 'crear_tareas.html', {'form': form})
    
def editar_tareas(request, pk):
    tareas = get_object_or_404(Tarea, pk=pk)
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tareas)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')
    else:
        form = TareaForm(instance=tareas)
    return render(request, 'editar_tareas.html', {'form': form, 'tareas': tareas})


def eliminar_tareas(request, pk):
    tareas = get_object_or_404(Tarea, pk=pk)
    if request.method == 'POST':
        tareas.delete()
        return redirect('lista_tareas')
    return render(request, 'eliminar_tareas.html', {'tareas': tareas})