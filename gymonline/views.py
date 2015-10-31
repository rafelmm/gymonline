# -*- coding: utf-8 -*-
from django.shortcuts import render
from datetime import date
from django.utils.timezone import now
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _

def home(request):
    today = date.today()
    return render(request, "gymonline/index.html", {'today': today, 'now': now()})

def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")


        