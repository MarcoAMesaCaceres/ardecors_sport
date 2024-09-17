from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import ArticleForm
from django.db.models import Q
from django.contrib import messages

def lista_articles(request):
    articles = Article.objects.all()
    return render(request, 'lista_articles.html', {'articles': articles})

def crear_articles(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'El artículo ha sido creado exitosamente.')
            return redirect('lista_articles')
        else:
            messages.error(request, 'Ha ocurrido un error al crear el artículo. Por favor, revise los campos.')
    else:
        form = ArticleForm()
    return render(request, 'crear_articles.html', {'form': form})

def editar_articles(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'El artículo ha sido actualizado exitosamente.')
            return redirect('lista_articles')
        else:
            messages.error(request, 'Ha ocurrido un error al actualizar el artículo. Por favor, revise los campos.')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'editar_articles.html', {'form': form, 'article': article})

def eliminar_articles(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        messages.success(request, 'El artículo ha sido eliminado exitosamente.')
        return redirect('lista_articles')
    return render(request, 'eliminar_articles.html', {'article': article})