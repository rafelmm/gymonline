# -*- coding: utf-8 -*-
"""gymonline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from .views import home, home_files, mision_vision

urlpatterns = [
    url(r'^(?P<filename>(robots.txt)|(humans.txt))$',
        home_files, name='home-files'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'i18n/', include('django.conf.urls.i18n')),
    
]

urlpatterns += i18n_patterns(
    url(r'^$', home, name='home'),
    url(r'^mision-vision/$', mision_vision, name='mision-vision'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^gymclient/', include('gymonline.apps.gymclient.urls',namespace="gymclient")),   
    url(r'^contact/', include('gymonline.apps.gymcontact.urls', namespace="gymcontact")),
    url(r'^gymadmin/', include('gymonline.apps.gymadmin.urls', namespace="gymadin")),
    url(r'^news/', include('gymonline.apps.gymnews.urls', namespace="gymnews")),
)
