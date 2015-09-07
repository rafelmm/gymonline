# -*- coding: utf-8 -*-
from django import forms
from gymonline.apps.gymclient import models

class ClaseForm(forms.ModelForm):
    class Meta:
        model = models.Clase
        exclude = ['fecha_modificacion']