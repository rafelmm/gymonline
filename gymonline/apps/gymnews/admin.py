# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

# Register your models here.
from .models import Article, Comment


class CommentInline(admin.StackedInline):
    model = Comment
    verbose_name_plural = _("Comments")
    extra = 1
    
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','publish_date','tags')
    list_filter = ['tags']
    search_fields = ['tags', 'author']
    inlines = (CommentInline, )

    
