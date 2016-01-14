# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from gymonline.apps.gymnews import managers
from django.conf import settings

# Create your models here.
class Article(models.Model):
    # Relations
    author = models.ForeignKey(
                        settings.AUTH_USER_MODEL,
                        related_name="article_author",
                        verbose_name=_("Author")
    )
    
    # Attributes - Mandatory
    title = models.CharField(max_length=150, verbose_name=_("Title"))
    publish_date = models.DateTimeField(verbose_name=_("Published at"), 
                                            auto_now_add=True)
    text = models.CharField(max_length=2500, verbose_name=_("Text"))
    
    # Attributes - Optional
    tags = models.CharField(max_length=500, verbose_name=_("Tags"))
    
    # Manager
    objects = managers.ArticleManager()
    
    # Functions  
    def __unicode__(self):
        return self.title

    # Meta
    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")
        ordering = ["-publish_date"]
        
class Comment(models.Model):
    # Relations
    article_id = models.ForeignKey(
                                    Article, 
                                    related_name="comment_article",
                                    verbose_name=_("Comment"))
    
    # Attributes - Mandatory
    email = models.EmailField(verbose_name=("Email"))
    date = models.DateTimeField(verbose_name=_("Published at"), 
                                            auto_now_add=True)
    
    text = models.CharField(max_length=500, verbose_name="Comment")
    
    # Manager
    objects = managers.CommentManager()
    
    # Functions
    def __unicode__(self):
        return self.text

    # Meta
    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
        ordering = ["date"]