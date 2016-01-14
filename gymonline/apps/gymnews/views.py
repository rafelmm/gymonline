# -*- coding: utf-8 -*-

from django.shortcuts import render

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Article
from .forms import ArticleForm

# Create your views here.

def article_list(request):
    articlelist = Article.objects.all()
    for article in articlelist:
        article.taglist = article.tags.split(',')
    return render(request,
                  "gymnews/article_list.html",
                  {'articlelist': articlelist}
                  )
    
def article_detail(request, articleid):
    articleid = int(articleid)
    article = get_object_or_404(Article, id=articleid)
    return render(request,
                  "gymnews/article_detail.html",
                  {'article': article}
                  )
    
def article_form(request, articleid=None):
    if request.method == "POST":
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            print(article_form.cleaned_data['text'])
            article = article_form.save()
            return HttpResponseRedirect(reverse('gymnews:article_list'))
    else:
        if articleid:
            article = get_object_or_404(Article, id=articleid)
            article_form = ArticleForm(instance=article)
        else:
            article_form = ArticleForm()
    
    return render(request,
                      "gymnews/article_form.html",
                      {'article_form': article_form}
                      )
def article_delete(request, articleid=None):
    articleid = int(articleid)
    Article.objects.get(id=articleid).delete()
    return HttpResponseRedirect(reverse('gymnews:article_list'))