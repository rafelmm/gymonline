# -*- coding: utf-8 -*-
from django.shortcuts import render
from datetime import date
def home(request):
    today = date.today()
    return render(request, "gymonline/index.html", {'today': today})

def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")