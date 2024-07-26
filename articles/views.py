from django.shortcuts import render, get_object_or_404
from .models import Article
from .forms import ArticleForm

def lista_articles(request):
    productos = Article.objects.all()
    return render(request, 'productos/lista_productos.html', {'productos': productos})

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Article, id=producto_id)
    return render(request, 'productos/detalle_producto.html', {'producto': producto})

def crear_producto(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirige a la lista de productos o a otro lugar
    else:
        form = ArticleForm()
    return render(request, 'productos/crear_producto.html', {'form': form})