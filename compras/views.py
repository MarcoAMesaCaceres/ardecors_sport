from django.shortcuts import get_object_or_404, redirect, render
from .models import Compras
from .forms import ComprasForm, ComprasSearchForm
from django.db.models import Q

def lista_compras(request):
    compras = Compras.objects.all()
    form = ComprasSearchForm(request.GET)
    
    if form.is_valid():
        search_query = form.cleaned_data.get('search_query')
        min_total = form.cleaned_data.get('min_total')
        max_total = form.cleaned_data.get('max_total')
        fecha_inicio = form.cleaned_data.get('fecha_inicio')
        fecha_fin = form.cleaned_data.get('fecha_fin')
        
        if search_query:
            compras = compras.filter(
                Q(proveedor__nombre__icontains=search_query) | 
                Q(producto__icontains=search_query)
            )
        
        if min_total:
            compras = compras.filter(total__gte=min_total)
        
        if max_total:
            compras = compras.filter(total__lte=max_total)
        
        if fecha_inicio:
            compras = compras.filter(fecha__gte=fecha_inicio)
        
        if fecha_fin:
            compras = compras.filter(fecha__lte=fecha_fin)
    
    return render(request, 'lista_compras.html', {'compras': compras, 'form': form})

# ... (resto de las vistas)
# compras/views.py

def crear_compras(request):
    if request.method == 'POST':
        form = ComprasForm(request.POST)
        if form.is_valid():
            compra = form.save()
            return redirect('lista_detalles_compra', compra_id=compra.id)
    else:
        form = ComprasForm()
    return render(request, 'crear_compras.html', {'form': form})

def editar_compras(request, pk):
    compra = get_object_or_404(Compras, pk=pk)
    if request.method == 'POST':
        form = ComprasForm(request.POST, instance=compra)
        if form.is_valid():
            form.save()
            return redirect('lista_compras')
    else:
        form = ComprasForm(instance=compra)
    return render(request, 'editar_compras.html', {'form': form, 'compra': compra})

def eliminar_compras(request, pk):
    compra = get_object_or_404(Compras, pk=pk)  # Cambiado de 'compras' a 'Compras'
    if request.method == 'POST':
        compra.delete()
        return redirect('lista_compras')  # Cambiado aquí
    return render(request, 'eliminar_compras.html', {'compra': compra})