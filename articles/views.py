from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import ArticleForm
from django.db.models import Q
from django.contrib import messages
from django.db import transaction
from django.core.exceptions import ValidationError

def lista_articles(request):
    id_query = request.GET.get('id', '')
    nombre_query = request.GET.get('nombre', '')
    descripcion_query = request.GET.get('descripcion', '')
    precio_query = request.GET.get('precio', '')
    stock_query = request.GET.get('stock', '')

    # Validación del ID
    if id_query and not id_query.isdigit():
        messages.error(request, "Debe colocar un número válido para el ID.")
        return render(request, 'lista_articles.html', {'articles': Article.objects.none()})

    articles = Article.objects.all()

    if id_query:
        articles = articles.filter(id=id_query)
    if nombre_query:
        articles = articles.filter(nombre__icontains=nombre_query)
    if descripcion_query:
        articles = articles.filter(descripcion__icontains=descripcion_query)
    if precio_query:
        articles = articles.filter(precio=precio_query)  # Si deseas un filtro exacto
    if stock_query:
        articles = articles.filter(stock=stock_query)  # Si deseas un filtro exacto

    # Validación: si no hay resultados después de la búsqueda
    if not articles.exists():
        messages.warning(request, "Este producto no existe en inventario.")

    return render(request, 'lista_articles.html', {'articles': articles})

@transaction.atomic
def crear_articles(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                article = form.save()
                messages.success(request, 'Artículo creado exitosamente.')
                return redirect('lista_articles')
            except ValidationError as e:
                messages.error(request, f'Error al crear el artículo: {e}')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = ArticleForm()
    return render(request, 'crear_articles.html', {'form': form})

@transaction.atomic
def editar_articles(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            try:
                article = form.save()
                messages.success(request, 'Artículo actualizado exitosamente.')
                return redirect('lista_articles')
            except ValidationError as e:
                messages.error(request, f'Error al actualizar el artículo: {e}')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'editar_articles.html', {'form': form, 'article': article})

@transaction.atomic
def eliminar_articles(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        try:
            # Verificar si hay ventas relacionadas
            if article.detalles_venta.exists():
                messages.error(request, 'No se puede eliminar el artículo porque tiene ventas asociadas.')
                return redirect('lista_articles')
            
            article.delete()
            messages.success(request, 'Artículo eliminado exitosamente.')
            return redirect('lista_articles')
        except Exception as e:
            messages.error(request, f'Error al eliminar el artículo: {e}')
    return render(request, 'eliminar_articles.html', {'article': article})



