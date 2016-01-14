# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from gymonline.apps.gymnews import views

urlpatterns = patterns('',
    url(r'^article/$', views.article_list, name="article_list"),
    url(r'^article/(?P<articleid>\d+)/$', views.article_detail, name="article_detail"),
    url(r'^new-article/$', views.article_form, name="article_form"),
    url(r'^edit-article/(?P<articleid>\d*)/$', views.article_form, name="article_form"),
    url(r'^delete-article/(?P<articleid>\d+)/$', views.article_delete, name="delete_article"),
)