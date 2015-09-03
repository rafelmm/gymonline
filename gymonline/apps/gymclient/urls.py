# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from gymonline.apps.gymclient import views
urlpatterns = patterns('',
    url(r'^$', views.home,name='home'),
    url(r'^clase/$', views.clase_list, name="clase_list"),
    url(r'^clase/(?P<id>\d+)/$', views.clase_detail, name="clase_detail"),
    url(r'^edit-clase/$', views.clase_form, name="clase_form"),
    url(r'^edit-clase/(?P<id>\d*)/$', views.clase_form, name="clase_form"),
)