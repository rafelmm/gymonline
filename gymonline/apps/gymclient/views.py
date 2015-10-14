# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from gymonline.apps.gymclient import models
from gymonline.apps.gymclient import forms

def home(request):
    return render(request, 
                  "home.html",
                  {}
                  )
    
def class_list(request):
    clase = models.GymClass.objects.all()
    return render(request,
                  "gymclient/clase_list.html",
                  {'claselist': clase}
                  )


def class_detail(request, classid):
    classid = int(classid)
    clase = get_object_or_404(models.GymClass, id=classid)
    return render(request,
                  "gymclient/clase_detail.html",
                  {'clase': clase}
                  )

def class_form(request, classid=None):
    if request.method == "POST":
        clase_form = forms.ClassForm(request.POST)
        if clase_form.is_valid():
            clase = clase_form.save()
            return HttpResponseRedirect(reverse('gymclient:home'))
    else:
        if classid:
            clase = get_object_or_404(models.GymClass, id=id)
            clase_form = forms.ClassForm(instance=clase)
        else:
            clase_form = forms.ClassForm()
        return render(request,
                      "gymclient/clase_form.html",
                      {'clase_form': clase_form}
                      )
