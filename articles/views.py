from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import ArticleForm


def lista_articles(request):
    articles = Article.objects.all()
    return render(request, 'lista_articles.html', {'articles': articles})

def detalle_articles(request, producto_id):
    article = get_object_or_404(Article, id=producto_id)
    return render(request, 'detalle_articles.html', {'article': article})

def crear_articles(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_articles.html')  # Cambia esto por la vista adecuada
    else:
        form = ArticleForm()
    return render(request, 'crear_articles.html', {'form': form})