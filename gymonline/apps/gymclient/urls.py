# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from gymonline.apps.gymclient import views
from .views import home

urlpatterns = patterns('',
    url(r'^$', home, name='home'),
    url(r'^profile/$', views.profile_form, name='profile_form'),
    url(r'^class/$', views.class_list, name="class_list"),
    url(r'^class/(?P<classid>\d+)/$', views.class_detail, name="class_detail"),
    url(r'^edit-class/$', views.class_form, name="class_form"),
    url(r'^edit-class/(?P<classid>\d*)/$', views.class_form, name="class_form"),
    
)