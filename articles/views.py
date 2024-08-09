from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import ArticleForm,ArticleSearchForm
from django.db.models import Q




def lista_articles(request):
    articles = Article.objects.all()
    form = ArticleSearchForm(request.GET)
    
    if form.is_valid():
        search_query = form.cleaned_data.get('search_query')
        min_price = form.cleaned_data.get('min_price')
        max_price = form.cleaned_data.get('max_price')
        
        if search_query:
            articles = articles.filter(
                Q(nombre__icontains=search_query) | 
                Q(descripcion__icontains=search_query)
            )
        
        if min_price:
            articles = articles.filter(precio__gte=min_price)
        
        if max_price:
            articles = articles.filter(precio__lte=max_price)
    
    return render(request, 'lista_articles.html', {'articles': articles, 'form': form})

def crear_articles(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_articles')
    else:
        form = ArticleForm()
    return render(request, 'crear_articles.html', {'form': form})

def editar_articles(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('lista_articles')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'editar_articles.html', {'form': form, 'article': article})

def eliminar_articles(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('lista_articles')
    return render(request, 'eliminar_articles.html', {'article': article})