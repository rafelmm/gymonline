# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from gymonline.apps.gymclient import models
from gymonline.apps.gymclient import forms

def home(request):
    return render(request, 
                  "gymclient/home.html",
                  {}
                  )


def clase_list(request):
    clase = models.Clase.objects.all()
    return render(request,
                  "gymclient/clase_list.html",
                  {'claselist': clase}
                  )


def clase_detail(request, id):
    id = int(id)
    clase = get_object_or_404(models.Clase, id=id)
    return render(request,
                  "gymclient/clase_detail.html",
                  {'clase': clase}
                  )

def clase_form(request, id=None):
    if request.method == "POST":
        clase_form = forms.ClaseForm(request.POST)
        if clase_form.is_valid():
            clase = clase_form.save()
            return HttpResponseRedirect(reverse('gymclient:home'))
    else:
        if id:
            clase = get_object_or_404(models.Clase, id=id)
            clase_form = forms.ClaseForm(instance=clase)
        else:
            clase_form = forms.ClaseForm()
        return render(request,
                      "gymclient/clase_form.html",
                      {'clase_form': clase_form}
                      )
