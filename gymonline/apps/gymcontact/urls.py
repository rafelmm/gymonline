# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from .views import home, contact_sended

urlpatterns = patterns('',
    url(r'^$', home, name='contact'),
    url(r'^send/', home, name='sendcontact'),
    url(r'^sended/', contact_sended, name='contact_sended'),
)